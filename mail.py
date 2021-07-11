# -*- coding: utf-8 -*-
# Author: coolrc <root@coolrc.me>
# date:   2021/7/11
"""Description"""

import unittest

from conf import config
from mailer import Mailer


class MailClient:
    def __init__(self):
        mail_conf = config['mail']
        self.mail = Mailer(**mail_conf)
        self.send = self.mail.send

    # def send_text(self, receiver: str, cc=None, bcc=None, subject: str = None, text: str = None) -> bool:
    #     return self.mail.send(receiver, cc, bcc, subject, message=text)
    #
    # def send_html(self, receiver: str, cc=None, bcc=None, subject: str = None, html: str = None) -> bool:
    #     return self.mail.send(receiver, cc, bcc, subject, html)


class TestMail(unittest.TestCase):
    def test_send_mail(self):
        client = MailClient()
        res = client.send(receiver='qq1782536964@live.com',  # Email From Any service Provider
                          subject='hi',
                          html='<h2>HI, This Message From Python :)</h2>')
        self.assertTrue(res)
