from flask_mail import Message
from flask import render_template

from app import mail
from manage import app


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['INDEX_FUND_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['INDEX_FUND_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)


__author__ = 'davidkarapetyan'
