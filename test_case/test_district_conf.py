# -*-coding: utf-8-*-
# @Author = jishanshan
# @Date = 2020/4/18
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import os
import sys
import time
import pytest


def test_login():
    print(sys.path)
    driver=webdriver.Chrome('D:\python_project\selenium_test\driver\chromedriver.exe').maximize_window()
    driver.maximize_window()

    driver.get('https://am-test.zuihuibao.com/zhb-pc-agency/#/')
    wait=WebDriverWait(driver,10)
    # wait.until()
    time.sleep(5)
    input_list=driver.find_elements_by_class_name('el-input__inner')
    submit=driver.find_elements_by_tag_name('button')[1]

    mobile=input_list[0]
    verify=input_list[1]
    mobile.send_keys('17621968863')
    # time.sleep(1)
    verify.send_keys('9527')
    # time.sleep(3)
    submit.click()
    # time.sleep(5)

    exit=wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,'login-out')))
    # time.sleep(5)
    assert exit

def test_issue_account():
    pass

