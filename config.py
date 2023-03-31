#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dotenv,os

# Load environment variables
dotenv.load_dotenv(verbose=True)

# Gmail server
gmail_server = "smtp.gmail.com"

# Gmail account
gmail_user = os.getenv("GMAIL_USER")

gmail_passwd = os.getenv("GMAIL_PASSWD")

# Outlook server
outlook_server = "smtp-mail.outlook.com"

# Outlook account
account_path = "./3000.csv"
from_account =  "0"
to_account = "1"
