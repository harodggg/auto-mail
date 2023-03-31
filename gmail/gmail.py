#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib


class Gmail:
    def __init__(self,username,passwd):
        self.username = username
        self.passwd = passwd
        self.server = NULL

    def login(self):
        print("%s,Logging in..." % self.username)
        try:
            self.server = smtplib.SMTP('smtp.gmail.com',587)
            self.server.starttls()
            self.server.login(self.username,self.passwd)
            print("%s,Login success" % self.username)
            return True
        except Exception as e:
            print(e)
            return False

    def get_all_email(self):
        print("Getting all email...")
        try:
            self.server.list()
            print("Get all email success")
            return True
        except Exception as e:
            print(e)
            return False

    def get_email_by_keyword(self,keyword):
        print("Getting email by keyword...")
        try:
            self.server.list()
            print("Get email by keyword success")
            return True
        except Exception as e:
            print(e)
            return False

    def close(self):
        self.server.close()


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


