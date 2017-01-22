#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/22 0022 上午 11:02
# @Author  : Trojx
# @File    : yue.py

import leancloud_object_define
from leancloud import *
#
# words=[]
# with open('./zidian_zhyue-kfcd/yue.txt') as f:
#     lines= f.readlines()
#     for line in lines:
#         jt=line.strip().split('	')[0]
#         ft=line.strip().split('	')[1]
#         yin=line.strip().split('	')[2]
#         word=(jt,ft,yin)
#         words.append(word)

query=Query('word')
query.exists('voiceFile')
print query.count()