FROM node:18-alpine

WORKDIR /srv/app

COPY ./package.json .

CMD npm install

COPY . .

EXPOSE 8011

CMD npm run build && npm run preview
