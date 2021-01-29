Usar docker:
    - Crear contenedores basados en imágenes existentes (REPO: docker hub)
        - Entorno aislado para el proceso que ejecuto
        - Una imagen de contenedor lleva dentro TODO lo necesario
    - Crear nuestras propias imagenes de contenedor: DOCKERFILE
        - Distribuir nuestro software de manera muy sencilla y robusta
    - Crear aplicaciones multicontenedor:
        - DOCKER-COMPOSE 
-----------------------
Usos de docker:
    Desarrollador:
        Generar un entorno de trabajo para mi: BBDD, Servidores de aplicaciones, Librerias, Drivers...
        Distribuir su software en contenedores
    Tester: 
        Generar un entorno de trabajo para mi: Selenium, Jmeter, appium...
            Ejemplo: pagina web
                Funcionales
                UI: Selenium
                    Varios navegadores (chrome, firefox, opera, ...).... en distintas versiones
                Rendimiento: Jmeter <<< JAVA
        Rapidez instalaciones, Entorno aislado, Consistencia en la distribución
-----------------------
Entorno de producción
    Alta disponibilidad (HA): Declaración de intenciones.... me dimensiono y acepto de antemano unos riesgos
        99% <<< 100 dias 1 puede caerse: 1 años: 3,5 dias abajo.
        99,9% <<< 1000 dias 1 puede caerse: 1 años: 8 horas abajo.
        99,99% <<< 1000 dias 1 puede caerse: 1 años: minutos abajo.
    Escalabilidad
        
    Clusters:
        Activo / Pasivo >>> HA
        Activo / Activo >>> HA + Escalabilidad

---------------------------------------
[Docker Swarm //] Kubernetes // Openshift

Estas herramientas son gestores de contenedores en cluster.

Docker swarm: Es de la propia gente de DOCKER
              Se basa en ficheros docker-compose.yml
              NO SE USA

------- SI SE USAN:
Kubernetes: Opensource + Freeware
    >>> Google

Openshift: Opensource + (SI y NO)... Por debajo lleva Kubernetes
    >>> Redhat
            Ansible + Ansible engine
            Ansible AWX + Ansible Tower
            Fedora + RHEL
            Wildfly + JBOSS
            Openshift origin + Openshift Container Platform
----------
    No están basadas en docker-compose.yml
    Estan basadas en ficheros según sintaxis "Kubernetes.yml"

    Hasta hace contados días, estas herramientas por debajo usaban DOCKER. Desde enero 2021 ya no.
---------- DOCKER
Docker cli
Docker-compose cli

Dockerd --- Servicio
    ContainerD
        runC
        runC
        runC
---------- KUBERNETES ANTES
kubectl --- cli
Kubelet --- Servicio
    Dockerd --- Servicio
        ContainerD
            runC
            runC
            runC
---------- KUBERNETES HOY EN DIA
kubectl --- cli
Kubelet --- Servicio
    ContainerD
        runC
        runC
        runC
----------
Opensource:
    El código está disponible para todo el mundo
    Es gratuito (No es cierto)
Freeware: 
    Es gratuito
    El código está disponible para todo el mundo (No es cierto)
----------

Principales diferencias al usar contenedores en un   entorno local   vs   entorno producción:
                                                       1 máquina          Varias máquina (cluster)

Despliegues con actualizaciones se deben hacer en todas las máquinas <<< Kubernetes se encarga de esto.
Uso de SERVICIOS con colas y balanceo de carga: SON GRATIS EN KUBERNETES / OPENSHIFT / SWARM
    ESCALABILIDAD ??? SOLUCIONADO:
        Estos gestores crearán contenedores bajo demanda (si hay hueco..)
    ALTA DISPONIBILIDAD ??? DEPENDE:
        EN PRINCIPIO SI:
            Si se cae un contenedor habrá otro... y si no lo hay, Kubernetes lo crea
                Si se cae la luz, nada impide a Kubernetes, que le dé un cluster deslocalizado:
                        - 4 máquinas en ESPAÑA
                        - 4 máquinas en USA
                        - 4 máquinas en Taiwán
        PERO...
            Tengo instalado en un contenedor MySQL:
                ¿Qué pasa si se cae el MySQL, si se jode la máquina?
                    A priori:: Levanto otro. ES ESTO SOLUCIÓN???
                        Dónde estaban los datos?
                            - Si están dentro del contenedor : RUINA !!! No lo voy a hacer
                                - Creo un VOLUMEN y así los datos no están en el contenedor....
                                    - Pero si creamos un VOLUMEN como lo hemos estado haciendo hasta ahora...
                                        - Los datos estarían en el host que se ha jodido... Se ha ido el HDD
                                        - RUINA !!!!!
                                    - Los VOLUMENES son EXTERNOS
        

----------
Supermercado(, Tienda)                                                              ---- Cluster físico
    Gerente: Controlando todo                                                       ---- Kubernetes / Openshift
        Pool                                                                        ---- Es dinámico. Creo a las personas bajo demanda, igual que las destruyo
            de personas con una serie de                                            ---- Contenedores
                HABILIDADES                                                               --- Imágenes 
    Carnicería   -   Fila única (Número, ticket) >>>>                               ---- Servicio que ofrece el cluster
                       Pantalla, La persona con el ticket: 12!!!!                   <<<< Cliente va al servicio, pido la vez, me pongo a la cola
        Carnicero(a)1  --- Puesto
                       --- Puesto                                                   ---- Ordenador, máquina 
    Frutería                                                                        ---- Servicio que ofrece el cluster
    Panadería
    Pescadería
    Droguería
    Cajas        -   Fila única >>>>>>>                                             ---- Servicio publicos que ofrece el cluster
                            Pantalla, Persona : A la 4!!!!                          ---- Balanceador de carga    
        Cajero1(a) --- CAJA FISICA 
        Cajero2(a) --- CAJA FISICA 
        Cajero3(a) --- CAJA FISICA 
        Cajero4(a) --- CAJA FISICA                                                  ---- Contenedor < Servicio
                   --- CAJA FISICA 
                   --- CAJA FISICA                                                  ---- Ordenador, máquina
                   
    Mozo(a) de almacén  <<< Hace su trabajo, pero no interactua con los clientes    ---- Contenedor < Servicio privados o Demonio
    Mozo(a) de almacén  <<< Hace su trabajo, pero no interactua con los clientes
    Mozo(a) de almacén  <<< Hace su trabajo, pero no interactua con los clientes
    
    Persona de limpieza <<< Hace su trabajo, pero no interactua con los clientes    ---- Contenedor < Demonio
    Persona de limpieza <<< Hace su trabajo, pero no interactua con los clientes
    
    Puerta de entrada al supermercado                                               ---- Ingress
        ROTULOS
            Pescaderia, siga la flecha....                                          --- contextos de URL
            Carnicería, siga la flecha....
            Frutería, siga la flecha....
    Puerta de entrada al almacen                                                    ---- Ingress
    Puerta de entrada a oficinas                                                    ---- Ingress
    
    http:/micluster.kubernets.prod/pescaderia >>>> Servicio   >>>> Contenedor
    
------------
Kubernetes
    Servicio: MySQL-service
        Puerto: 3000
        Cola y un balanceador
        
        Contenedor: MySQL-container: 3306

    Servicio: Webapp-service
        Contenedor: Webapp-container:8080
            Conecta con el servicio: MySQL-service
----------
    Servicio: MySQL-service
        Puerto: 3000
        Cola y un balanceador
    Servicio: Webapp-service
        Puerto: 80
        Cola y un balanceador
    Contenedor: MySQL-container: 3306
    Contenedor: Webapp-container:8080
