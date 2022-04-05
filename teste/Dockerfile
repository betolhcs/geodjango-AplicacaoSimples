FROM python:3.8
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

WORKDIR /Django/teste

COPY requirements.txt ./
RUN pip install -r requirements.txt

#Bibliotecas Geo Espaciais
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin 

CMD python manage.py runserver 0:8000