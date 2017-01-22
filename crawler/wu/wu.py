#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/18 0018 下午 12:04
# @Author  : Trojx
# @File    : wu.py
import requests


if __name__ == '__main__':
    res=requests.get('http://wu-chinese.com/minidict/search.php?searchkey=%E8%8F%9C&searchlang=zaonhe&category=')
    print res.content