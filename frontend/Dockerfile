FROM node:18-alpine

WORKDIR /srv/app

COPY . .

EXPOSE 8001

CMD npm install && npm run build && npm run preview
