# ACC-Mini-Project

Run Celery and RabbitMQ with Docker, and generate worker clusters

steps.sh is used to prepare meshes for calculation and make airfoil available for execution

convert.py is used to convert all .msh files into .xml files

To run the project, enter celery folder and do following commands
```bash
docker-compose build
docker-compose up --scale worker=1

docker exec -it celery_worker_1 /bin/bash
python3 run.py
```
There's gonna be 1 celery_worker docker container and 1 rabbitmq docker container with the calculation solving in rabbitmq server.
