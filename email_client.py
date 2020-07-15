#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib

class SMTPClient(object):

    def __init__(self):
        self.HOST = 'localhost'
        self.PORT = 1025
        self.sender = 'hilmarhergeirs@gmail.com'
        self.receivers = ['alerts@example.com']

    def send_email(self, sender, receivers, template):
        print('Sending to email addresses: %s' % receivers)
        try:
            client = smtplib.SMTP(self.HOST, self.PORT)
            client.sendmail(sender, receivers, template)         
            print('Successfully sent email')
        except SMTPException:
            print('Error: Unable to send email')

    def send_support_email(self, service):
        message = """From: Hilmar Hergeirsson <{}>
            To: Alerts <{}>
            Subject: Service failure: {}

            Message: {}
            Number of errors: {}
            """
        self.send_email(
            self.sender,
            self.receivers,
            message.format(self.sender, self.receivers[0], service['service_id'], service['status']['message'], service['events']['error'])
        )
