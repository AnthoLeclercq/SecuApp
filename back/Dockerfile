FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y nmap

COPY . .

RUN pip install -r requirements.txt

COPY /app/. .

ENV FLASK_APP=main.py
#créé le dossier pour les rapports
ENV PATH_REPORT_FOLDER=/var/reports
RUN mkdir -p /var/reports

# Exécuter les migrations de base de données
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

EXPOSE 5001

CMD [ "python", "main.py" ]