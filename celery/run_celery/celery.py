from celery import Celery

app = Celery('run_celery', broker='amqp://u:p@rabbit:5672', backend='rpc://', include=['run_celery.tasks'])
