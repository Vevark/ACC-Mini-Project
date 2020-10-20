# ACC-Mini-Project

Run Celery and RabbitMQ with Docker, and generate worker clusters

steps.sh is used to prepare meshes for calculation and make airfoil available for execution

convert.py is used to convert all .msh files into .xml files

To run the project, enter celery folder and do following commands
```bash
docker-compose build
docker-compose up --scale worker=2

docker exec -it docker_worker_1 /bin/bash
docker exec -it docker_worker_2 /bin/bash
```
copy needed xml files into worker containers, run
```bash
python3 run_1.py
```
and
```bash
python3 run_2.py
```
in different worker containers

There's gonna be 2 docker_worker docker containers and 1 rabbitmq docker container with the calculation solving on rabbitmq server.
