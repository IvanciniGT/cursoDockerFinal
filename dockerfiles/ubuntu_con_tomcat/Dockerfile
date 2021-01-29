# Establece la imagen de base de nuestra imagen de contenedor
FROM ubuntu

# Actualizar repos e instalar telnet y ping
RUN apt-get update
RUN apt-get install default-jdk -y
RUN apt-get install curl -y

RUN (cd /tmp && curl -O https://ftp.cixug.es/apache/tomcat/tomcat-8/v8.5.61/bin/apache-tomcat-8.5.61.tar.gz)

RUN mkdir /opt/tomcat
RUN tar xzvf /tmp/apache-tomcat-8*tar.gz -C /opt/tomcat --strip-components=1
RUN chmod u+x /opt/tomcat/conf

# ENV: Setea una variable de entorno en el contenedor temporal
#      Que además es mantenida en los contenedores posteriores
# ARG: Setea una variable de entorno en el contenedor temporal
#      Que NO es mantenida en los contenedores posteriores

#ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64/jre
ENV CATALINA_PID=/opt/tomcat/temp/tomcat.pid
ENV CATALINA_HOME=/opt/tomcat
ENV CATALINA_BASE=/opt/tomcat
ENV CATALINA_OPTS='-Xms512M -Xmx1024M -server -XX:+UseParallelGC'
ENV JAVA_OPTS='-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'


# Indicar el comando/ programa que quiero que se ejecute
CMD ["/bin/bash","-c","/opt/tomcat/bin/startup.sh && sleep infinity"]


