#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib


class Gmail:
    def __init__(self,username,passwd):
        self.username = username
        self.passwd = passwd
        self.server = logging(username,passwd)
    
    def login(self)


def logging(username,passwd):
    print("%s,Logging in..." % username)
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(username,passwd)
        print("%s,Login success" % username)
        print(server)
        return server
    except Exception as e:
        print(e)
        return False


def get_email():
    print("获取邮件")


