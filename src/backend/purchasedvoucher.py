from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from os import environ

app = Flask(__name__)
##Rememeber to change db connection using environ
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@pvdb:3306/purchasedvoucher'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)  

#creating a AvailableVoucher object 
# class AvailableVoucher(db.Model):
#     __tablename__ = 'AvailableVoucher'

#     PlatformName = db.Column(db.String(50), nullable=False, primary_key=True)
#     DiscountAmt = db.Column(db.Integer, nullable=False, primary_key=True)
#     DDRequired = db.Column(db.Integer, nullable=False)


#     # purchasedvouchers=db.relationship('PurchasedVoucher', backref='AvailableVoucher')
    

#     #init AvailableVoucher object
#     def __init__(self, PlatformName, DDRequired, DiscountAmt):
#         self.PlatformName=PlatformName
#         self.DiscountAmt=DiscountAmt

#         self.DDRequired=DDRequired

#     #returned object in JSON format
#     def json(self):
        
#         return {
#             'PlatformName': self.PlatformName,
#             'DiscountAmt': self.DiscountAmt,
#             'DDRequired': self.DDRequired
#         }

#creating a PurchasedVoucher object 
class PurchasedVoucher(db.Model):
    __tablename__ = 'purchasedVoucher'

    Vid=db.Column(db.Integer, autoincrement=True, primary_key=True)
    Uid=db.Column(db.Integer)
    # Uid=db.Column(db.ForeignKey("User.UID", ondelete='CASCADE', onupdate="CASCADE") )
    PlatformName=db.Column(db.String(50))
    DiscountAmt=db.Column(db.Integer)
    DDRequired= db.Column(db.Integer)
    # PlatformName = db.Column(db.String(50), db.ForeignKey("AvailableVoucher.PlatformName", ondelete='CASCADE', onupdate="CASCADE"))
    # DiscountAmt = db.Column(db.String(20), db.ForeignKey('AvailableVoucher.DiscountAmt', ondelete='CASCADE', onupdate="CASCADE"))
    # Cost = db.Column(db.Integer, db.ForeignKey('AvailableVoucher.Cost', ondelete='CASCADE', onupdate="CASCADE"))
    PurchasedDate= db.Column(db.DateTime, nullable=True, default=datetime.now)
    RedeemedDate=db.Column(db.DateTime, nullable=True)
    ExpiryDate= db.Column(db.DateTime, nullable=False)

    
    # rs=db.relationship('AvailableVoucher', backref='AVAILABLEVOUCHERS', primaryjoin='AvailableVoucher.PlatformName==PurchasedVoucher.PlatformName && AvailableVoucher.DiscountAmt==PurchasedVoucher.DiscountAmt && AvailableVoucher.Cost==PurchasedVoucher.Cost')
    # pname_rs=db.relationship('AvailableVoucher', backref='PlatformName', uselist=False, foreign_keys=[PlatformName])
    # discamt_rs=db.relationship('AvailableVoucher', backref='DiscountAmt', uselist=False, foreign_keys=[DiscountAmt])
    # cost_rs=db.relationship('AvailableVoucher', backref='Cost', uselist=False, foreign_keys=[Cost])



    

    #init PurchasedVoucher object. PurchasedDate, RedeemedDate and ExpiryDate are left blank (idk how we gonna set the date lmao)
    def __init__(self,Uid,PlatformName, DiscountAmt, DDRequired, ExpiryDate):
        # self.Vid=Vid
        self.Uid=Uid
        self.PlatformName=PlatformName
        self.DiscountAmt=DiscountAmt
        self.DDRequired=DDRequired
        self.ExpiryDate=ExpiryDate
    
        

    #returned object in JSON format
    def json(self):
        
        return {
            'Vid': self.Vid,
            'Uid': self.Uid,
            'PlatformName': self.PlatformName,
            'DiscountAmt': self.DiscountAmt,
            'DDRequired': self.DDRequired,
            'PurchasedDate' : self.PurchasedDate,
            'RedeemedDate': self.RedeemedDate,
            'ExpiryDate': self.ExpiryDate
        }
with app.app_context():
    db.create_all()

#function to get all purchased vouchers according to Uid:
@app.route('/purchasedvoucher/<int:uid>', methods=['GET'])
def get_purchased_vouchers(uid):
    all_purchased_voucher_list=PurchasedVoucher.query.filter_by(Uid=uid).all()
    #query need to filter and show redeemable vouchers (redeemedDate should be empty for redeemable vouchers)
    if len(all_purchased_voucher_list):
        return jsonify(
            {
                "code":200,
                "data": {
                    "AllVouchers": [voucher.json() for voucher in all_purchased_voucher_list]
                }
            }
        )
    
    #else: no purchased vouchers
    return jsonify(
        {
            'code':404,
            "message": "There are no available vouchers."
        }
    )


#function to change the redeemedDate. Occurs when user redeemed a voucher. 
@app.route('/purchasedvoucher/<int:VID>', methods=['PUT'])
def redeem_voucher(VID):
    selected_voucher= PurchasedVoucher.query.filter_by(Vid=VID).first()

    #redeem voucher and input the redeemed date.
    if selected_voucher:
        selected_voucher.RedeemedDate= datetime.utcnow()
        db.session.commit()
        return jsonify(
            {
                "code":200,
                "data": selected_voucher.json()
            }
        )
    
    return jsonify(
        {
            'code': 404,
            'message': 'Error redeeming voucher'
        }
    )



@app.route('/purchasedvoucher', methods=['POST'])
def add_voucher():
    # /<string:pname>/<string:discount>/<int:uid>/<int:cost>
    
    data = request.get_json()
    
    # print(data)
    # #querying for the parent voucher in AvailableVoucher db
    # parent_voucher=AvailableVoucher.query.filter_by(PlatformName=data['pname'], DiscountAmt=data['discount'], DDRequired=data['DDRequired']).first()
    # print(parent_voucher)
    
    # #chosen voucher is not in available voucher db
    # if not parent_voucher:
    #     return jsonify(
    #         {
    #             "code": 500,
    #             "message":  "Chosen voucher not found in the AvailableVoucher database."
    #         }

    #     )
    
    #chosen voucher is in available voucher DB:
    #currently expiry date is current timing. Need to fix this!!!
    expiry_date= datetime.utcnow()
    # self,Uid,PlatformName, DiscountAmt, Cost, ExpiryDate
    # Uid,PlatformName, DiscountAmt, Cost, ExpiryDate
    added_voucher=PurchasedVoucher(Uid=data['uid'], PlatformName=data['pname'], DiscountAmt=data['discount'], DDRequired=data['DDRequired'],ExpiryDate=expiry_date  )
    db.session.add(added_voucher)
    db.session.commit()
    return jsonify(
        {
            "code": 200,
            "data": added_voucher.json()
        }
    )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)