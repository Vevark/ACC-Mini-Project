from celery import Celery
import os

app = Celery('tasks', broker='amqp://u:p@rabbit:5672', backend='rpc://')

@app.task
def cal(xmlfile):
    os.system('./navier_stokes_solver/airfoil 10 0.0001 10. 1 '+xmlfile)
