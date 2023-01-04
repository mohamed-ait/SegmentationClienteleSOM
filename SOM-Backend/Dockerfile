FROM python:3.10.7
#copier le fichier requirements.txt qui contient les dépendances puis les installer
COPY requirements.txt .
RUN pip  install -r requirements.txt
# Copy the current directory contents into the container at /app
COPY . /app
#Définir le répertoire de travail de l'application
WORKDIR /app
EXPOSE 8000
# Run the command to start uvicorn when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]