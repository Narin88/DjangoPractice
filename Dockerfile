FROM python:3.9-slim-buster

RUN apt-get update

RUN apt-get install -y git

RUN apt-get update && apt-get install -y libaio1 wget unzip

WORKDIR /opt/oracle

RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip && \
    unzip instantclient-basiclite-linuxx64.zip && rm -f instantclient-basiclite-linuxx64.zip && \
    cd /opt/oracle/instantclient* && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci && \
    echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig
    
RUN python -m pip install cx_Oracle

WORKDIR /home/

RUN git clone https://github.com/Narin88/DjangoPractice.git

WORKDIR /home/DjangoPractice/

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage,py", "runserver", "0.0.0.0:8000"]