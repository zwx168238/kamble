#!/usr/bin/python
#coding=utf-8

import hashlib
import os
import re
import signal
import sqlite3
import subprocess
import sys
import time
import base64
from argparse import ArgumentParser

from BeautifulSoup import BeautifulSoup
from selenium import webdriver

web_addr = "https://github.com/login"

class userinfo(object):
    def __init__(self, web_addr, name,password):
        self.web_addr = web_addr
        self.name = name
        self.password = password

def get_info():
    name = base64.encodestring(raw_input("input username: "))
    password = base64.encodestring(raw_input("input password: "))
    info = userinfo(web_addr,base64.decodestring(name),base64.decodestring(password))

def login(userinfo):
    driver = webdriver.Firefox()
    driver.get(info.web_addr)
    elem = driver.find_element_by_name("login")
    elem.send_keys(info.name)
    print name 
    elem =driver.find_element_by_name("password")
    print password
    elem.send_keys(info.password)
    elem = driver.find_element_by_name("commit")
    elem.click()
    time.sleep(5)
    driver.quit()
if __name__ == "__main__":
    print "*************************************************"
    name = base64.encodestring(raw_input("input username: "))
    password = base64.encodestring(raw_input("input password: "))
    info = userinfo(web_addr,base64.decodestring(name),base64.decodestring(password))
    login(info)
    print "*************************************************"
