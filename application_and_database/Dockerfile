FROM ubuntu
RUN mkdir /home/app
WORKDIR /home/app
COPY murtazo.tgz /home/app
COPY app.py /home/app
RUN apt-get update
RUN apt-get -y upgrade 
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install flask
CMD ["python3","app.py"]
