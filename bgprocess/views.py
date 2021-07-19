from apscheduler.triggers.cron import CronTrigger
from django.utils import timezone
from django.utils.crypto import get_random_string
from rest_framework import generics, status
from rest_framework.response import Response

from bgprocess.management.commands.runapscheduler import scheduler
from .utils import Util


def my_job(job_id):
    # Your job processing logic here...
    print('running from my_job ' + job_id)


def scheduled_email(to, subject, body):
    Util.sendgrid_email({
        'email_subject': subject,
        'email_body': body,
        'to_email': to
    })


class SendMailAPIView(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        # scheduler.add_job(
        #     my_job,
        #     args=(job_id,),
        #     trigger=CronTrigger(second="*/10"),  # Every 10 seconds
        #     id=job_id,  # The `id` assigned to each job MUST be unique
        #     max_instances=1,
        #     replace_existing=True,
        # )
        time = timezone.now() + timezone.timedelta(minutes=1)
        scheduler.add_job(
            scheduled_email,
            args=(request.data['to'], request.data['subject'], request.data['body']),
            trigger=CronTrigger(minute=time.minute),
            id=get_random_string(),
            max_instances=1,
            replace_existing=True,
        )

        return Response({'message': 'scheduled'}, status=status.HTTP_200_OK)
