#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/14 0014 上午 11:56
# @Author  : Trojx
# @File    : frovo.py
from pymongo import *
from leancloud_object_define import *
from multiprocessing import Pool
import leancloud
import urllib, requests, time
from hanziconv import HanziConv

leancloud.init('6vNrCi5ou4rw5sb0fx8b0J4w-gzGzoHsz', 'zfuBYXx8X235VVi6O7acOM8G')

client = MongoClient('localhost', 27017)
db = client['fangyan']
col_word = db['word']

zh_lang_code = ['fzho', 'wuu', 'hak', 'pcc', 'cjy', 'zh', 'hsn', 'yue', 'gan', 'cdo', 'nan']
zh_lang_name = [u'福州话', u'吴语', u'客家话', u'布依语', u'晋语', u'汉语', u'粤语', u'赣语', u'闽东语', u'闽南语']


def get_lang_word_list(lang_code, page_count):
    for i in range(1, page_count + 1):
        url = 'http://zh.forvo.com/languages-pronunciations/' + lang_code + '/page-' + str(i) + '/'
        print url


def get_all_word_and_save():
    skip = 0
    limit = 1000

    while True:
        query = leancloud.Query('word')
        query.limit(limit)
        query.skip(skip)
        print skip
        lc_words = query.find()
        if len(lc_words) > 0:
            for lc_word in lc_words:
                col_word.insert_one({'name': lc_word.get('name'), 'leanCloudId': lc_word.id})
            skip += limit
        else:
            exit(0)


def get_word_has_no_page():
    words = col_word.find({'page_html': {'$exists': False}})
    return words


def get_word_page_and_save(a_word):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/54.0.2840.59 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch'}

    try:
        response = requests.get('http://zh.forvo.com/word/' + a_word['name'], headers=headers)
        a_word['page_html'] = response.content
        print 'status_code=>' + str(response.status_code)
    except IOError, e:
        print e
        return
    col_word.save(a_word)
    time.sleep(5)
    print 'saving=>' + a_word['name']


if __name__ == '__main__':
    # print 'words remain=>'+str(col_word.count({'page_html':{'$exists':False}}))
    # words = get_word_has_no_page()
    # pool = Pool(2)
    # pool.map(get_word_page_and_save, words)
    for w in col_word.find({'name':True,'name_trad':True}):
        w['name_trad'] = HanziConv.toTraditional(w['name'])
        print w['name_trad']
        col_word.save(w)
    print 'done'
