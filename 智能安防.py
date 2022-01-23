# -*- coding = utf-8 -*-
# @Time : 2022/1/22 9:00
# @Author : xiuyifan
# @File : 智能安防.py
# @Software : PyCharm
import pandas as pd
import requests
import re
import time
import os
import lxml
from lxml import etree
from lxml import etree
import selenium
from selenium import webdriver
#延时机制的简单爬取

#json方式是解析不了代码的
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
proxies ={
    'http':'http://122.136.124.80:8060',
    'http':'http://117.28.134.177:15233',
    'http':'http://42.7.90.139:17655',
    'http':'http://117.57.41.59:18534',
    'http':'http://117.42.243.65:15632',
    'http':'http://218.91.7.95:15081',
    'http':'http://114.96.168.23:20290',
    'http':'http://114.226.163.115:23621',
    'http':'http://111.126.93.17:19553',
    'http':'http://27.29.146.175:23127',
    'http':'http://175.44.109.236:16727',
    'http':'http://42.179.197.40:20833',
    'http':'http://60.169.114.239:16710',
    'http':'http://114.237.29.217:17816',
    'http':'http://183.93.200.50:22499',
    'http':'http://220.201.23.90:19585',
    'http':'http://122.239.130.220:23553',
    'http':'http://27.156.142.96:16886',
    'http':'http://110.90.222.242:18083',
    'http':'http://114.99.15.60:15561',
    'http':'http://119.142.79.133:23524',
    'http':'http://123.180.69.198:19095',
    'http':'http://111.127.119.140:1887',
}
for pages in range(1,9):
    url = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100009219666&score=1&sortType=5&page={pages-1}&pageSize=10&isShadowSku=0&fold=1'
    response = requests.get(url = url, headers=headers,proxies=proxies).text
    response = response.replace('fetchJSON_comment98(','')
    response = response.replace(');','')
    comm_data = json.loads(response)
    comm_list = comm_data['comments']
    cont = [comm['content'] for comm in comm_list]
    color = [comm['productColor'] for comm in comm_list]
    size = [comm['productSize'] for comm in comm_list]
    days = [comm['days'] for comm in comm_list]
    time.sleep(1)
    imageCount = [comm.get('imageCount')  for comm in comm_list]
    nickname = [comm['nickname'] for comm in comm_list]
    replies_list = [comm.get('replies') for comm in comm_list]
    #整个list都为空
    re_content = ['' if rep==None or len(rep)==0 else rep[0]['content'] for rep in replies_list]
    score = [comm['score'] for comm in comm_list]
    usefulVoteCount = [comm['usefulVoteCount'] for comm in comm_list]

    # 将list放入dataframe
    comment_data = pd.DataFrame({'用户名':nickname, '评论':cont,'颜色':color,'产品尺寸':size, '得分': score, '有用':usefulVoteCount,'时间':days, '回复': re_content,'图片数':imageCount })
    comment_data.index = comment_data.index + 1 #是将index变成1 不然之前是以0开头。
    comment_data.to_csv('./智能安防2差.csv',mode='a',header=0,encoding='ANSI')
    time.sleep(3)

# 可能需要进行模拟登录才可以爬取全部内容。
