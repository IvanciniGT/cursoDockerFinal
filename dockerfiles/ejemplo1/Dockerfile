# Establece la imagen de base de nuestra imagen de contenedor
FROM ubuntu

# Copiar un archivo al contenedor: micomando.sh
COPY micomando.sh /

# Actualizar repos e instalar telnet y ping
RUN apt-get update
RUN apt-get install telnet -y
RUN apt-get install iputils-ping -y
VOLUME ["/datos","/configuracion"]
# Indicar el comando/ programa que quiero que se ejecute
CMD ["/micomando.sh"]

#docker run --name MI_CONTENEDOR -v /home/usuario/datos:/datos \
#                                -v /home/usuario/conf:/configuracion \
#                                ESTA_IMAGEN

#docker run --name MI_CONTENEDOR ESTA_IMAGEN
#               >>>>> Docker va a generar unas carpetas independientes en el FileSystem del HOST, pero que yo 
#                     No tengo a priori ni idea de donde están. 
#-------------------------
# Establece la imagen de base de nuestra imagen de contenedor
#FROM ubuntu

# Copiar un archivo al contenedor: micomando.sh
#COPY micomando.sh /

# Actualizar repos e instalar telnet y ping
#RUN apt-get update
#RUN apt-get install telnet -y
#RUN apt-get install iputils-ping -y
# Indicar el comando/ programa que quiero que se ejecute
#CMD ["/micomando.sh"]

#EXPOSE 1276    
# 

#docker run --name MI_CONTENEDOR ESTA_IMAGEN
#docker run --name MI_CONTENEDOR -v /home/usuario/datos:/datos \
#                                -v /home/usuario/conf:/configuracion \
#                                ESTA_IMAGEN
# En este caso, docker toma esas carpetas del HOST y las comparte en el contenedors,
# IGUAL que si hubiera definido los volumenes.

# Para que quiero definir los VOLUMENES en el DOCKERFILE ??? BUEN GUSTO, DOCUMENTACION, TRAZA
# Que quede constancia de que yo guardo ahñi cosas que requieren PERSISTENCIA

#--------------
#FROM ubuntu
#RUN apt-get update
#RUN apt-get install apache2 -y   # Instalaría un Apache Web server
# EXPOSE 80 443
#--------------
# Que puertos hay funcionando??? 80 y 443
# OJO: NO HE DEFINIDO UN EXPOSE
# Pregunta: PUEDO ACCEDER A DICHOS PUERTOS DESDE FUERA DEL CONTENEDOR?
#           Sin problema!
# Quién sería el único que haría que esos puertos sean accesibles o no?
#           Un firewall que montara dentro
#--------------
#FROM ubuntu
#EXPOSE 80 443
#--------------
# Que puertos hay funcionando??? NINGUNO
    # No hay ningún programa abriendo esos puertos
    
#----------
# Que pinta el EXPOSE ??? Para que sirve?  
        # BUEN GUSTO, DOCUMENTACION, TRAZA
        # Que quede constancia de que yo abro ese puerto, para que los servicios que hubiera automáticos, sepan donde atacar