# coding=UTF-8
from selenium import webdriver
import time
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sys

browser = webdriver.Chrome()
browser.maximize_window()

def test_login():
    # print os.environ
    browser.get('https://www.zuihuibao.cn/brokera_channels/#/login?jup=jup&source=new')

    time.sleep(2)
    # wait=ui.WebDriverWait(browser,10)
    # wait.until(lambda browser: browser.find_element_by_class_name('sms_w').is_displayed())

    user_name=browser.find_element_by_xpath('/html/body/div/div/div/div/div/input')
    user_pwd=browser.find_element_by_class_name('sms_w')
    login_btn=browser.find_element_by_class_name('login_btn')
    yzm_btn=browser.find_element_by_class_name('yzm_btn') # 获取验证码按钮
    x_btn=browser.find_element_by_class_name('login_fix_box').find_element_by_tag_name('i') #弹框关闭按钮
    eval_input=browser.find_element_by_class_name('login_fix_box').find_element_by_tag_name('input')  #输入验证码框
    tj_btn=browser.find_element_by_class_name('tj_btn') #确定按钮
    user_name.send_keys('10000000999')
    time.sleep(1)

    # 打开图形验证码弹框
    # yzm_btn.click()
    # # time.sleep(1)
    # wait = ui.WebDriverWait(browser, 10)
    # wait.until(lambda browser: browser.find_element_by_class_name('login_fix_box').find_element_by_tag_name('input').is_displayed())
    # eval_input.send_keys('1234')
    # tj_btn.click()
    # # time.sleep(3)
    # # 点击对话框中的链接
    # # 由于对话框中的元素被蒙板所遮挡，直接点击会报 Element is not clickable的错误
    # # 所以使用js来模拟click
    # # 在watir-webdriver中只需要fire_event(:click)就可以了
    # browser.execute_script('arguments[0].click()', x_btn)
    # x_btn.click()
    user_pwd.send_keys('9527')
    time.sleep(1)

    # print login_btn.is_enabled()

    browser.execute_script('document.getElementsByClassName("login_btn")[0].click()')
    # browser.execute_script('$(arguments[0]).click()', login_btn)
    # print login_btn.is_displayed()

    # if login_btn.is_enabled():
    # login_btn.click()
    time.sleep(3)

    print browser.title
    # browser.quit()

def test_main_page():
    # browser.get('https://www.zuihuibao.cn/brokera_channels/#/home?source=new')
    # action = ActionChains(browser)

    city_province=browser.find_element_by_id('city_province')
    city_province.click()
    time.sleep(1)
    e_province=browser.find_element_by_xpath("//ul[@class='wheel-scroll wheel-scroll-hook']/li[text()='江苏']")
    e_province.click()
    time.sleep(1)
    e_city_list=browser.find_elements_by_class_name('wheel-scroll-hook')[1].find_elements_by_tag_name('li')
    for city in e_city_list:
        print city.get_attribute("style")

    # e_city = browser.find_element_by_xpath("//ul[@class='wheel-scroll wheel-scroll-hook']/li[text()='南京']")
    # e_city.click()
    time.sleep(1)
    confirm_hook=browser.find_element_by_class_name('confirm-hook')
    confirm_hook.click()
    # browser.fullscreen_window()



def select_provice_city():
    pass

def select_district():
    pass

def test_banner():
    pass


if __name__=='__main__':
    test_login()
    test_main_page()