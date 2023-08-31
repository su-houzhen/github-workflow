#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import yagmail
import random
import time
import os
import json

email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

# glados 签到 url
url = "https://glados.rocks/api/user/checkin"
cookies = {
    "koa:sess": "eyJ1c2VySWQiOjM4Mzg4NSwiX2V4cGlyZSI6MTcxOTM5NzgwNTg2NywiX21heEFnZSI6MjU5MjAwMDAwMDB9",
    "koa:sess.sig": "yIGXjzGJaGkG06usfNfX07Tg60A",
    "__stripe_mid": "66fe41cb-0264-4356-91c1-e066e104abbe25967c"
}
# from 请求负载
value = {"token": "glados.one"}

# wait some times
time.sleep(random.randint(30, 300))

result = requests.post(url, cookies=cookies, data=value)
result_json = result.json()

print(result_json)

code = result_json['code']
message = result_json['message']

msg = {
    "status": code,
    "message": message
}

#print(msg)

yag = yagmail.SMTP(user=email, password=password, host='smtp.163.com')
yag.send(to=email, subject='glados sign in', contents=msg)
