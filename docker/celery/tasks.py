from celery import Celery
import os

app = Celery('tasks', broker='amqp://u:p@rabbit:5672', backend='rpc://')

@app.task
def cal_1():
    os.system('./navier_stokes_solver/airfoil 10 0.0001 10. 1 r0a0n200.xml')

@app.task
def cal_2():
    os.system('./navier_stokes_solver/airfoil 10 0.0001 10. 1 r0a3n200.xml')
