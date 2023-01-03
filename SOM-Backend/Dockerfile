FROM python:3.8
#copier le fichier requirements qui contients les dépendances puis les installer
COPY requirements.txt .
RUN pip install -r requirements.txt
#copier le reste des fichiers de l'application
COPY . .
#Définir le répertoire de travail de l'application
WORKDIR /app
#Définir le port de l'application :
EXPOSE 8082
#Définir l'entrepoint de l'application
ENTRYPOINT["python"]
#Définir le script principal de l'application
CMD ["main.py"]