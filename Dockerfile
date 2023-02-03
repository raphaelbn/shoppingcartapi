FROM python:3.11.1

EXPOSE 80 8000

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# System Deps
RUN apt-get update && apt-get install && apt-get clean

ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

ADD . /usr/src/app/

ENTRYPOINT ["python", "/usr/src/app/manage.py"]
