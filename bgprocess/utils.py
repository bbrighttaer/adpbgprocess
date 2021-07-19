import os

from django.core.mail import EmailMessage
from rest_framework.exceptions import APIException
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Util:

    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['email_body'],
            to=(data['to_email'],))
        email.send()

    @staticmethod
    def sendgrid_email(data):
        message = Mail(
            from_email=os.environ.get('EMAIL_HOST_USER'),
            to_emails=data['to_email'],
            subject=data['email_subject'],
            html_content=data['email_body'])

        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            return response
        except Exception as e:
            raise APIException(str(e))
