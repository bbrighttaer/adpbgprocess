from django.apps import AppConfig
from django.core.management import call_command
from threading import Thread


def start_scheduler():
    call_command('runapscheduler')


class BgprocessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bgprocess'

    def ready(self):
        super().ready()
        t = Thread(target=start_scheduler)
        t.start()
