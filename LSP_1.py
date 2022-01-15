# -*- coding = utf-8 -*-
# @Time : 2022/1/14 13:23
# @Author : xiuyifan
# @File : LSP_1.py
# @Software : PyCharm

import requests
import re
import os
import lxml
from lxml import etree

    if not os.path.exists('./piclibs'):
        os.mkdir('./piclibs')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}


url = 'https://pic.netbian.com/4kmeinv/index_22.html'
response = requests.get(url=url, headers=headers)
#手动设定响应数据的编码格式
#response.encoding = 'utf-8'
page_text = response.text

#数据解析： src的属性值 和 alt的属性值
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]/ul[@class="clearfix"]//li')
for li in li_list:
    img_src = 'https://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
#注意做局部数据解析的时候要用./
#注意SRC的属性值不是一个完整的域名
    img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
    #通用处理中文乱码的方式
    img_name = img_name.encode('iso-8859-1').decode('gbk')

# 请求图片并进行持久化存储
    img_data = requests.get(url=img_src,headers=headers).content
    img_path = 'piclibs/'+img_name
    with open(img_path,'wb') as fp:
        fp.write(img_data)
        print(img_name,'保存成功')







