#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dotenv,os

# Load environment variables
dotenv.load_dotenv(verbose=True)

# Gmail server
GMAIL_SERVER = "smtp.gmail.com"

# Gmail account
GMAIL_USER = os.getenv("GMAIL_USER")

GMAIL_PASSWD = os.getenv("GMAIL_PASSWD")

# Outlook server
OUTLOOK_SERVER = "smtp-mail.outlook.com"

# Outlook account
ACCOUNT_PATH = "./3000.csv"
ACCOUNT_FROM =  "0"
ACCOUNT_TO = "1"
