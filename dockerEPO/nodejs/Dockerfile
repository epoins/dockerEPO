# Utiliser l'image officielle de Node.js comme base
FROM node:23

# Définir le répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# Copier le fichier package.json et installer les dépendances
COPY package*.json ./
RUN npm install

# Copier le reste des fichiers de l'application
COPY . .

# Exposer le port sur lequel l'application écoute
EXPOSE 3000

# Définir la commande pour démarrer l'application
CMD ["npm", "start"]

