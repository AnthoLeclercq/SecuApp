# Image de base Node.js Alpine plus légère
FROM node:18-alpine

# Set working directory
WORKDIR /app

COPY scanreport/public/ /app/public
COPY scanreport/src/ /app/src
COPY scanreport/package*.json /app/
COPY scanreport/tsconfig.json /app/
COPY scanreport/.env /app/

# Installation des dépendances
RUN apk add --no-cache build-base && npm install

# Exécution de l'application
EXPOSE 3000
CMD [ "npm", "start" ]