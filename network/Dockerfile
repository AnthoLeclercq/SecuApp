FROM alpine:latest


# Mettre à jour les paquets et installer Apache
RUN apk update && apk upgrade && \
    apk add --no-cache apache2

COPY apache.conf /etc/apache2/conf.d/apache.conf

ENV APACHE_LOG_DIR /var/log/apache2

# Exposer le port HTTP
EXPOSE 80

# Démarrer Apache au lancement du conteneur
CMD ["httpd", "-D", "FOREGROUND"]
