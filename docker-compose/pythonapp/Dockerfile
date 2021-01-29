FROM python:3

WORKDIR /usr/src/app

RUN pip install mysql-connector-python

COPY programa.py .
#COPY wait-for-it.sh .

ENV DB_HOST=mysql
ENV DB_USUARIO=usuario
ENV DB_PASSWORD=password

CMD [ "python", "./programa.py" ]