import imaplib
import outlook.login as outlook

imapserver = 'outlook.office365.com'
password="bqwK6dvW"
username="nxpbxqkdj@outlook.com"

def main():
    conn = imaplib.IMAP4_SSL(imapserver)
    conn.login(username,password)
    conn.list()   
    conn.select('INBOX')    #选择收件箱（默认）
    result , dataid = conn.uid ('search' , None , "ALL" )
    mailidlist = dataid[0].split() 
    print(mailidlist)

if __name__ == '__main__':
    print('start')
    cookies = outlook.get_cookie()
    print(cookies)
