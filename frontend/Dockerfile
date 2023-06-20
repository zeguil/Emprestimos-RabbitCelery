
FROM node:14-alpine


WORKDIR /app


COPY package*.json ./


RUN npm install

RUN npm install -g npm@9.7.1


COPY . .


RUN npm run build

CMD [ "npm", "run", "serve" ]
