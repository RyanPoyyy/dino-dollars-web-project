FROM node:18-slim
WORKDIR /app
COPY package*.json ./
# RUN npm install package_name --force
RUN npm install --force
COPY graphqlserver.js ./
EXPOSE 5030
CMD [ "node", "graphqlserver.js" ]