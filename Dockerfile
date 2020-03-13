FROM debian:latest AS pythonFlaskSH
MAINTAINER DANIEL BRITO ZENDEJAS <danielbrzen@outlook.com>
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY softhHealthAPI.py /app/softhHealthAPI.py
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["softhHealthAPI.py"]

#INICIALISA UNA NUEVA CONSTRUCCION DEL DOCKER 
FROM centos/mysql-80-centos7 AS mysqlSH 
## DATOS PARA SOPORTE DE LA IMAGEN DOCKER
MAINTAINER DANIEL BRITO ZENDEJAS<danielbrzen@outlook.com>

## VARIABLES DE ENTORNO PARA EL SERVIDOR MYSQL 
ENV MYSQL_DATABASE softhHealth
ENV MYSQL_USER shuser
ENV MYSQL_PASSWORD c8ee894bd2bd
ENV MYSQL_ROOT_PASSWORD 0d988e46bdfb
ENV MYSQL_HOME var/lib/mysql/

## COPIA EL ESQUEMA DE LA BASE DE DATOS SQL Y LO GUARDA EN LA CARPETA DE MYSQL PARA 
## UTILISARLO POSTERIORMENTE
COPY  SH_DB_SCHEMA.sql ${MYSQL_HOME}
WORKDIR /${MYSQL_HOME}


VOLUME [ "/mysqldata" ]

## EXPONE EL PUERTO 3306 DE NUESTRO CONTENEDOR AL HOST LOCAL
EXPOSE 3306
## COMPONE EL SCHEMA A LA BASE DE DATOS DEL CONTENEDOR DESDE UNA TERMINAL 
# cat sql_schema.sql | docker exec -i mysqlLecturaEscritura mysql -u root  lecturaEscritura



