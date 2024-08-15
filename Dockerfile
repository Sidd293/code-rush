# Use the official Node.js image as base
FROM docker:latest
RUN apk add --update nodejs npm
RUN apk add --update npm


WORKDIR /app

COPY package*.json ./

RUN npm i --production --legacy-peer-deps

COPY . .

EXPOSE 5000

CMD ["npm", "start"]
