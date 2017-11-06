#coding:utf-8
from selenium import webdriver
import time

dirver = webdriver.Firefox()
dirver.get("http://www.toutiao.com/")


time.sleep(1)
for i in range(10):
    # 模拟浏览器跳转到最底
    dirver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
