import requests
import sys
import json
import socket
from os.path import dirname, realpath
from sys import executable


def connect():
    try:
        hostname = socket.gethostname()
        my_ip = socket.gethostbyname(hostname)
    except:
        sys.exit(-1)

    path = dirname(realpath(executable)) + r'\user_info.json'
    url = 'http://10.99.99.99:8010/cgi-bin/webauth/ajax_webauth'
    data = json.load(open(path))
    user = data['user']
    pwd = data['pwd']

    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '358',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '10.99.99.99:8010',
        'Origin': 'http://47.98.217.39',
        'Referer': 'http://47.98.217.39/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47'
    }

    data = {
        'action': 'login',
        'user': user,
        'pwd': pwd,
        'usrmac': '30:5f:77:d9:28:01',
        'ip': my_ip,
        'success': 'http://47.98.217.39/lfradius/libs/portal/unify/portal.php/login/success/nastype/Panabit/basip/10.99.99.99/usrip/' + my_ip,
        'fail': 'http://47.98.217.39/lfradius/libs/portal/unify/portal.php/login/fail'
    }

    try:
        response = requests.post(url, headers=header, data=data).status_code
        return response
    except:
        sys.exit(-1)


def check_data():
    path = dirname(realpath(executable)) + r'\user_info.json'
    data = json.load(open(path))
    user = data['user']
    pwd = data['pwd']
    url = "http://47.98.217.39/lfradius/home.php?a=userlogin&c=login"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Length": "44",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "portal_wifi_connect=1; lf_timeout=1655378535",
        "Host": "47.98.217.39",
        "Origin": "http://47.98.217.39",
        "Referer": "http://47.98.217.39/lfradius/login.php?c=login&a=showlogin",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53",
    }
    datas = {
        "a": "userlogin",
        "c": "login",
        "username": user,
        "password": pwd,
    }
    try:
        user_pass = False
        response = requests.post(url=url, headers=headers, data=datas)
        cookies = response.cookies.items()
        for cookie in cookies:
            if cookie[0] == "check_user_pass":
                user_pass = True
        return user_pass
    except:
        sys.exit(-1)
