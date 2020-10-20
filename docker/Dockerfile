FROM quay.io/fenicsproject/stable:current
USER root
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install celery

ADD ./celery /app/
ADD ./navier_stokes_solver /app/navier_stokes_solver/
WORKDIR /app/

ENTRYPOINT celery -A tasks worker --concurrency=20 -l INFO
