import os

from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alco.settings')

app = Celery('alco')


app.config_from_object('django.conf:settings', namespace='CELERY')




app.conf.beat_schedule = {
    
    'cron':{
        'task':'celery_tasks.tasks.unblock_ip',
        'schedule':crontab(minute="*/1")
    }
    
}


app.autodiscover_tasks()


