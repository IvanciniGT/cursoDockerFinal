# Tomar imagen base
# nginx
FROM nginx
# instalar git
RUN apt-get update
RUN apt-get install git -y
# descargar proyecto dentro
# mediante git clone URL_REPO PATH
RUN rm -rf /usr/share/nginx/html
RUN git clone https://github.com/IvanciniGT/webEjemploAnsible \
    /usr/share/nginx/html