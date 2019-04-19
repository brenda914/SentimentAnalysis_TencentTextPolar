# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:44:17 2019

@author: ltt's pc
"""
import pandas as pd
import hashlib
import time
import random
import string
from urllib.parse import quote

def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))
    # Uppercase the md5 
    return m.hexdigest().upper()
 
def get_params(plus_item):
    # get the timestamp  
    t = time.time()
    time_stamp=str(int(t))
    # get the randome str 
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    # fill in your key and id of tencent
    app_id = 'XXXXX'
    app_key = 'XXXXX'
    params = {'app_id':app_id,
              'text':plus_item,
              'time_stamp':time_stamp,
              'nonce_str':nonce_str,
              
              }
    sign_before = ''
    # sort the params and concate them  
    for key in sorted(params):
        # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。  
        sign_before += '{}={}&'.format(key,quote(params[key], safe=''))
    # concate app_key with sign_before  
    sign_before += 'app_key={}'.format(app_key)
    # use the curlmd5 fuction to calculate the sign  
    sign = curlmd5(sign_before)
    params['sign'] = sign
    return params


import requests

def get_content(plus_item):
    # the API of the text polar
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textpolar"
    # request 
    plus_item = plus_item.encode('utf-8')
    payload = get_params(plus_item)
    
    r = requests.post(url,data=payload)
    return r.json()

print(get_content('今天天气真好'))


