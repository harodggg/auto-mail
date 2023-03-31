#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imaplib
import outlook.login as outlook
import gmail.login as gmail
import config

imapserver = 'outlook.office365.com'
password="bqwK6dvW"
username="nxpbxqkdj@outlook.com"

def main():
    conn = imaplib.IMAP4_SSL(imapserver)
    conn.login(username,password)
    conn.list()
    conn.select('INBOX')
    result , dataid = conn.uid ('search' , None , "ALL" )
    mailidlist = dataid[0].split()
    print(mailidlist)

if __name__ == '__main__':
#    cookies = outlook.get_cookie()
#    print(cookies)
    gmail.logging(config.GMAIL_USER,config.GMAIL_PASSWD)


