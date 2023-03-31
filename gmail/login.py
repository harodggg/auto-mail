#!/usr/bin/env python

import smtplib

def logging(username,passwd):
    print("%s,Logging in..." % username)
    try:
        print("hello")
    except Exception as e:
        print(e)
        return False


def get_email():
    print("获取邮件")


