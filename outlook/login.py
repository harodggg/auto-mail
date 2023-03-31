#/usr/bin/env python3

from fake_useragent import UserAgent
import requests

def get_cookie():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    url = 'https://login.live.com'
    session = requests.Session()
    session.post(url, headers=headers)
    cookie = session.cookies.get_dict()
    return cookie

def loging_email(cookie,login,passwd):
    url = 'https://login.live.com/ppsecure/post.srf'
    headers = {
        'User-Agent': ua.random
    }
    data = {
        'login': login,
        'passwd': passwd}
    session = requests.Session()
    session.post(url, headers=headers, data=data, cookies=cookie)


