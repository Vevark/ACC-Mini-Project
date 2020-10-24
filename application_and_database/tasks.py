from celery import Celery
import os
import time

client = Celery("compute_forces", backend = "rpc://", broker="pyamqp://u:p@rabbit:5672//")

@client.task
def compute_forces():
    # Needs to be modified, this code is only for testing purposes
    #os.system("./navier_stokes_solver/airfoil 10 0.0001 10. 1 ./navier_stokes/r2a15n200.xml")
    time.sleep(10)
    result = "939394888 530200220030 43948430038403\n9232320 3023920390 239203239\n374328498 4932893894 4244322"
    return(result)
