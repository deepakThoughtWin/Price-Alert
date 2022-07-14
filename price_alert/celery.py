import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'price_alert.settings')

app = Celery('price_alert',broker_url='redis://redis:6379')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    #Scheduler Name
    'fetch-bitcoin-price-seconds': {
        # Task Name (Name Specified in Decorator)
        'task': 'get_realtime_price_tasks',  
        # Schedule      
        'schedule': 2.0,
        # Function Arguments 
    },
}  