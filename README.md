# TD7A4 #

## Prérequis
Avant de commencer, vous devez avoir installé les outils suivants sur votre système :

- Docker
- Docker compose

##  Cloner le dépôt

Tout d'abord, clonez le référentiel contenant notre image Docker et la configuration Docker Compose :

`git clone https://github.com/Alexis-Alaoui/TD7A4.git`

Et allez dans le nouveau répertoire

`cd TD7A4`

##  Créer un réseau de pont

Créez un réseau de ponts avec le nom de votre choix. Nous choisissons my-network ici.

`docker network create --driver bridge my-network`

##  Exécutez vos propres conteneurs
###  Sans Docker Compose

####  Télécharger l'image mongo

Extrayez de Dockerhub la dernière image mongo.

`docker pull mongo`

####  Exécutez le conteneur mongo sur votre réseau

`docker run --name my-mongo -d --network my-network mongo`

Remplacez my-mongo par le nom de votre choix pour votre conteneur mongo.

####  Créez l'image Docker de votre application

Ensuite, construisez l'image Docker avec votre Dockerfile :

`docker build -t my-app .`

Remplacez my-app par le nom souhaité pour votre image.

####  Lier le montage

Pour que le montage lié fonctionne, nous avons besoin d'un emplacement où une copie de data.txt est placée, donc lorsque ce fichier est mis à jour, la page Web contiendra les modifications. Nous avons choisi ici notre bureau.

`cp data.txt /Users/<your username>/Desktop`

Remplacez <votre nom d'utilisateur> par votre nom d'utilisateur.

####  Exécuter un conteneur à l'aide de l'image Docker

Pour exécuter un conteneur à l'aide de l'image Docker, utilisez la commande suivante :

`docker run --name my-flask-app -d --network network1 -p 5001:5000 -v /Users/<your username>/Desktop/data.txt:/app/data.txt my-app`

Remplacez my-flask-app par le nom souhaité pour votre conteneur et my-app par le nom de l'image Docker que vous avez créée précédemment.
Remplacez "votre nom d'utilisateur" par votre nom d'utilisateur.

Maintenant que nos deux conteneurs fonctionnent, vous pouvez consulter votre page Web sur localhost:5001. Sur la route par défaut, vous pouvez voir le contenu de votre base de données mongo, et sur la route /td6, le contenu de votre fichier data.txt.

Si vous modifiez le fichier data.txt dans votre bureau, enregistrez-le et actualisez votre page Web, vous verrez les modifications.

###  Utilisation de Docker Compose

Au lieu d'exécuter des conteneurs manuellement, vous pouvez utiliser Docker Compose pour gérer vos conteneurs plus facilement.

####  Exécuter les conteneurs

Pour créer votre image Docker et exécuter les conteneurs définis dans la configuration Docker Compose, utilisez la commande suivante :

`docker-compose up --build`

Maintenant, notre application s'exécute sur localhost : 5000

Sur la route par défaut, vous pouvez voir le contenu de votre base de données, et sur la route /td6 le contenu de data.txt.
Si vous modifiez le data.txt dans votre répertoire TD7A4, enregistrez-le et actualisez votre page, les modifications apparaîtront.

####  Arrêtez les conteneurs

Pour arrêter les conteneurs, utilisez la commande suivante :

`docker-compose down`

Cela arrêtera et supprimera tous les conteneurs définis dans la configuration Docker Compose.

Toutes nos félicitations! Vous avez maintenant créé et exécuté avec succès des conteneurs à l'aide de notre image Docker et de Docker Compose.
