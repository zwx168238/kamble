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
from argparse import ArgumentParser

from BeautifulSoup import BeautifulSoup
from selenium import webdriver

web_addr = "https://github.com/login"
name ="zwx168238@gmail.com"
password ="1qaz!QAZ"

def login():
    driver = webdriver.Firefox()
    driver.get(web_addr)
    elem = driver.find_element_by_name("login")
    elem.send_keys(name)
    print name 
    elem =driver.find_element_by_name("password")
    print password
    elem.send_keys(password)
    elem = driver.find_element_by_name("commit")
    elem.click()
    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    login()

