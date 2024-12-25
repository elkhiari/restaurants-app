# Restaurants

## Description

resturants est une application permettant de rechercher des restaurants proches en fonction de la localisation de l'utilisateur. Elle utilise **NestJS** pour le backend avec **MongoDB** comme base de données, et **Expo** pour le frontend mobile avec **Redux Toolkit** et **RTK Query** pour la gestion d'état et des appels API.

## Technologies utilisées

### Backend (NestJS)

- **NestJS** : Framework backend pour Node.js
- **MongoDB** : Base de données NoSQL pour stocker les informations des restaurants
- **Mongoose** : ODM pour MongoDB, permettant d'interagir avec la base de données de manière simple

### Frontend (Expo)

- **Expo** : Framework pour développer des applications mobiles avec React Native
- **Redux Toolkit (RTK)** : Gestion d'état et requêtes API via RTK Query
- **i18n-js** : Gestion des traductions de l'application
- **Reactotron** : Pour le débogage de l'application

## Fonctionnalités

1. **Recherche de restaurants** : Permet à l'utilisateur de rechercher des restaurants proches de sa position en utilisant la géolocalisation.
2. **Ajout de restaurants** : Permet d'ajouter plusieurs restaurants dans la base de données via une requête API.
3. **Affichage de la liste de restaurants** : Affiche la liste des restaurants disponibles dans la base de données.

## Installation

### Prérequis

Avant d'installer l'application, assurez-vous que vous avez les outils suivants installés sur votre machine :

- **Node.js** (version 18 ou supérieure)
- **npm** (version 8 ou supérieure)
- **MongoDB** ou une instance MongoDB hébergée (ex. MongoDB Atlas)
- **Expo CLI** (pour le frontend)

### Backend (NestJS)

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/elkhiari/restaurants-app.git
   cd restaurants-app/restaurants_back
   ```

2. Installez les dépendances :

   ```bash
    npm install
   ```

3. Créez un fichier .env à la racine du répertoire restaurants-back avec votre URI MongoDB :

   ```bash
    MONGO_URI=mongodb+srv://<your-connection-string>
   ```

4. Lancez le serveur :
   ```bash
   npm run start:dev
   ```

### Frontend (Expo)

1. Clonez le dépôt :

   ```bash
   cd ../restaurants-front
   ```

2. Installez les dépendances :

   ```bash
    npm install
   ```

3. Créez un fichier .env à la racine du répertoire restaurants-back avec votre URI MongoDB :

   ```bash
    EXPO_PUBLIC_API_URL=http://<ip>:3000
   ```

4. Lancez le serveur :

   ```bash
   npm start
   ```

5. Installation d'Expo Go

Avant de tester l'application, vous devez installer **Expo Go** sur votre appareil mobile.

- **Pour Android**, téléchargez et installez Expo Go depuis le [Google Play Store](https://play.google.com/store/apps/details?id=host.exp.exponent).
- **Pour iOS**, téléchargez et installez Expo Go depuis l'[App Store](https://apps.apple.com/us/app/expo-go/id982107779).
