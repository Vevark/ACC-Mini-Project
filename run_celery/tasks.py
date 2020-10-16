from .celery import app
import os

@app.task
def run():
    os.system('./murtazo/navier_stokes_solver/airfoil  10 0.0001 10. 1 ./murtazo/cloudnaca/msh/r2a15n200.xml')
