from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@userdb:3306/user'

db = SQLAlchemy(app)

CORS(app)  

class User(db.Model):
    __tablename__ = 'USER'
    UID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(64), nullable=False)
    Email = db.Column(db.String(64), nullable=False)
    Points = db.Column(db.Integer)
    Password= db.Column(db.String(64), nullable=False)

    # def __init__(self, UID, Name, Email, Points):
    #     self.UID = UID
    #     self.Name = Name
    #     self.Email = Email
    #     self.Points = Points

    def __init__(self, Name, Email, Password):
        # self.UID = UID
        self.Name = Name
        self.Email = Email
        self.Points = 0
        self.Password=Password

    def json(self):
        user = {"UID": self.UID, "Name": self.Name, "Email": self.Email, "Points": self.Points, 'Password':self.Password}
        user['LinkedAccs'] = []
        # for acc in self.ACCOUNTS:
        #     user['LinkedAccs'].append(acc.json())
        return user


class Accounts(db.Model):
    __tablename__ = 'ACCOUNTS'
    AID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UID = db.Column(db.ForeignKey('USER.UID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    Name = db.Column(db.String(64))

    def __init__(self, UID, Name):
        self.UID = UID
        self.Name = Name

    accs = db.relationship(
        'User', primaryjoin='Accounts.UID == User.UID', backref='ACCOUNTS')

    def json(self):
        return {"UID": self.UID, "Name": self.Name}

with app.app_context():
    db.create_all()

    if len(User.query.all()) == 0:
        u1 = User(Name="Ding", Email="gerald.ding.2021@scis.smu.edu.sg", Password="password")
        u2 = User(Name="Poy", Email="ryanpoy.2021@scis.smu.edu.sg", Password="password")
        a1 = Accounts(UID=1, Name="Facebook")
        a2 = Accounts(UID=1, Name="Google")

        db.session.add(u1)
        db.session.add(u2)
        db.session.add(a1)
        db.session.add(a2)
        db.session.commit()

@app.route('/user', methods=['GET'])
def get_all():
    userList = User.query.all()
    if len(userList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "users": [user.json() for user in userList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no users."
        }
    ), 404


@app.route("/user/<string:email>/<string:password>")
def find_by_email_and_password(email, password):
    # data=request.get_json()
    # Email=data['Email']
    # Password=data['Password']
    user = User.query.filter_by(Email=email , Password=password).first()

    #### I'm commenting this out temporarily
    # if user:
    #     return jsonify(
    #         {
    #             "code": 200,
    #             "data": user.json()
    #         }
    #     )
    # return jsonify(
    #     {
    #         "code": 404,
    #         "message": "User not found."
    #     }
    # ), 404
    if user:
        return jsonify(
            {
                "code": 200,
                "data": user.json()
            }
        ),200
    # print(user)
    return jsonify(
        {

            "code":404,
            "message": "Email or password incorrect."
        }
    ), 404


@app.route("/user/<int:UID>")
def find_by_UID(UID):
    user = User.query.filter_by(UID=UID).first()

    if user:
        return jsonify(
            {
                "code": 200,
                "data": user.json()
            }
        ),200
    print(user)
    return jsonify(
        {
            "code":404,
            "message": "UID not found."
        }
    ),404

    


# @app.route("/user/<int:UID>", methods=['POST'])
@app.route("/user", methods=['POST'])
def create_user():
    data = request.get_json()

    #checking for registration fields
    if data['Name'].strip()=="" or data['Password'].strip()=="" or data['Email'].strip()=="":
        return jsonify(
        {
            "code": 400,
            "message": "Registration failed. Please enter all fields"
        }
        ), 400
    
    #checking if username or email already exist in the database
    if (User.query.filter_by(Email=data['Email']).first()):
        return jsonify(
            {
                "code": 400,
                "message": "Email already exists."
            }
        ), 400
    
    if (User.query.filter_by(Name=data['Name']).first()):
        return jsonify(
            {
                "code": 400,
                "message": "Name already exists."
            }
        ), 400
    
    

    #the data should be in {username, email, password} format
    # print(data)
    user = User( Name=data['Name'], Email=data['Email'], Password=data['Password'])
    # print(user.Password)
    # print(user.Email)
    # print(user.Name)
    # print(user.UID)

    try:
        db.session.add(user)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the user."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": user.json()
        }
    ), 201


@app.route("/point/<int:UID>", methods=['PUT'])
def update_user(UID):
    try:
        user = User.query.filter_by(UID=UID).first()
        
        if not user:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "user": user
                    },
                    "message": "user not found."
                }
            ), 404

        # update status
        data = request.get_json()
        if data['Points']>0:
            user.Points = data['Points']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": user.json()
                }
            ), 200
        else:
            user.Points=0
            print(user)
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": user.json()
                }
            ), 200
            
        
        

    
        
    
        
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "user": user
                },
                "message": "An error occurred while updating the points. " + str(e)
            }
        ), 500


@app.route("/user/<int:UID>", methods=['DELETE'])
def delete_user(UID):
    user = User.query.filter_by(UID=UID).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "UID": UID
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "UID": UID
            },
            "message": "User not found."
        }
    ), 404

@app.route("/accounts/<int:UID>/<string:Name>", methods=['POST'])
def create_account(UID,Name):
    if (Accounts.query.filter_by(UID=UID, Name=Name).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "UID": UID,
                    "Name": Name
                },
                "message": "User has already linked account."
            }
        ), 400

    # data = request.get_json()
    account = Accounts(UID, Name)

    try:
        db.session.add(account)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "UID": UID,
                    "Name": Name
                },
                "message": "An error occurred linking the account."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": account.json()
        }
    ), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
