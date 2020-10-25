# ACC-Mini-Project

In this project, we use Celery as workers, RabbitMQ as the broker, Flask as the application and  MariaDB as the database. How the overall service workflow works can be seen in figure below.

<div style="text-align:center"><img src="end-user.png" alt="workflow" width=50% /></div>

1.  enter <code>blackbox</code> folder, run following commands
    ```bash
    sudo bash
    chmod +x requirements.sh
    ./requirements.sh
    ```
    get the <code>CONTAINER_ID</code> of FEniCS, and <code>docker exec -it CONTAINER_ID /bin/bash</code> to enter it. Then run 
    ```bash
    chmod +x steps.sh
    ./steps.sh
    ```
    inside the container, to have mesh files and the solver well-prepared. Then exit the container and copy them to <code>/docker/celery/</code> folder for further using. Arguments related to generating mesh files can be modified in steps.sh.

2.  Build app and worker images by <code>docker-compose build</code>

    Start all services with N workers by <code>docker-compose up --scale worker=N</code> 

3.  Enter one worker by <code>docker exec -it docker_worker_run_1 /bin/bash</code> and call Celery task by <code>python3 run.py mesh_xml/NAME_OF_A_MESH_XML_FILE</code>. <code>NAME_OF_A_MESH_XML_FILE</code> is any mesh file existing in <code>mesh_xml</code>

    Celery will distribute tasks to workers. Messages about overall calculation process can be shown through RabbitMQ.
