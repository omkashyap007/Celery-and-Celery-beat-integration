from __future__ import absolute_import , unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE" , "TaskProject.settings")

app = Celery("TaskProject")

app.conf.enable_utc = False

app.conf.update(timezone = "Asia/Kolkata")

app.conf.beat_schedule = {
    "every-1-minute" : {
        "task" : "base.tasks.getApiData" , 
        "schedule" : crontab(minute = "*/1") ,  
        "args" : () , 
        "kwargs" : {} , 
    }
}

app.config_from_object(settings,namespace= "CELERY")

app.autodiscover_tasks()