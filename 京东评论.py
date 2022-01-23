# -*- coding = utf-8 -*-
# @Time : 2022/1/19 18:01
# @Author : xiuyifan
# @File : 京东评论.py
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

商品编码 = input('请输入商品编码：')
#input输入进来的都是字符串。需要将其转换为数字
for 页数 in range(1,4):
    url = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={商品编码}&score=0&sortType=5&page={页数-1}&pageSize=10&isShadowSku=0&fold=1'
    #f 格式化字符串
    response = requests.get(url=url, headers=headers).text
    response = response.replace('fetchJSON_comment98(','')
    response = response.replace(');','')
    #将json数据转换为字典数据
    data = json.loads(response)
    comment_list = data['comments']
    #这种形式直接保存为列表，最终目的是放入pandas
    cont = [comm['content'] for comm in comment_list]
    color = [comm['productColor'] for comm in comment_list]
    size = [comm['productSize'] for comm in comment_list]
    # 将list放入dataframe
    comm_data = pd.DataFrame({'comments':cont,'color':color,'size':size})
    comm_data.index = comm_data.index + 1 #是将index变成1 不然之前是以0开头。
    comm_data.to_csv('./jingdong.csv',mode='a',header=0,encoding='ANSI')
    time.sleep(3)





