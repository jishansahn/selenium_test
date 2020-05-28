# -*-coding: utf-8-*-
# @Author = jishanshan
# @Date = 2020/4/19
import time
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

insure_data={
    "applicant": {
        "birthday": "1990-04-15",
        "certNo": "320826199004151424",
        "certType": "SFZ",
        "certValidateType": "Y",
        "email": "jishanshan@zuihuibao.com",
        "gender": "F",
        "mobile": "17621968863",
        "name": "吉姗姗"
    },
    "insurants": [
        {
            "birthday": "1985-06-19",
            "bnfList": [],
            "certNo": "340602198506192039",
            "certType": "SFZ",
            "certValidateType": "Y",
            "gender": "M",
            "hasSocialInsurance": "Y",
            "name": "杨勤光",
            "relation": "coupon"
        }
    ],

}

def test_product_list():
    try:
        driver=Chrome('D:\python_project\selenium_test\driver\chromedriver.exe')
        driver.maximize_window()
        driver.get('https://www.zhbbroker.cn/zhb-m-non-vehicle/#/')
        print(driver.current_window_handle)
        driver.add_cookie({"name":"ZHBSESSID","value":"aed6574ae2eb4887a3dd9ce9f582b770"})
        driver.get('https://www.zhbbroker.cn/zhb-m-non-vehicle/#/list-product')
        # driver.switch_to.window()
        wait=WebDriverWait(driver,5)
        load_e=wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,'product_detail')))
        assert load_e
        iyunbao_e=driver.find_elements(By.CLASS_NAME,'product_detail')[1]
        print(driver.window_handles)
        # driver.set_window_position(50,1000)
        # ActionChains(driver).move_to_element()
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # driver.execute_script('$(arguments[0]).click()',iyunbao_e)
        # ActionChains(driver).click(iyunbao_e).perform()
        iyunbao_e.click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        assert expected_conditions.title_contains('尊享e生')
        driver.save_screenshot('iyunbao_1.png')

        tb_btn=driver.find_element_by_class_name("za-button.theme-default.size-md.shape-rect")
        tb_btn.click()
        time.sleep(2)
        driver.save_screenshot('iyunbao_2.png')

        by_btn=driver.find_element_by_class_name("za-button.button-buy.theme-default.size-md.shape-rect")
        by_btn.click()
        time.sleep(2)
        driver.save_screenshot('iyunbao_3.png')

        no_btn=driver.find_element_by_class_name("button.button-2")
        no_btn.click()
        time.sleep(2)
        driver.save_screenshot('iyunbao_4.png')

        no2_btn=driver.find_element_by_class_name("button.button-2")
        no2_btn.click()
        time.sleep(2)
        driver.save_screenshot('iyunbao_5.png')

        driver.find_element_by_id('detail.applicant[name]').send_keys(insure_data["applicant"]["name"])
        driver.find_element_by_id('detail.applicant[certNo]').send_keys(insure_data["applicant"]['certNo'])
        driver.find_element_by_xpath("//div[@class='panel-body'][1]//div[text()='本人']").click()
        assert wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,'za-popup')))

        driver.find_element_by_xpath("//div[@class='za-popup']//div[text()='父母']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='za-popup']//div[text()='确定']").click()
        driver.find_element_by_id('detail.insurants[0][name]').send_keys(insure_data["insurants"][0]["name"])
        driver.find_element_by_id('detail.insurants[0][certNo]').send_keys(insure_data["insurants"][0]["certNo"])
        time.sleep(1)
        driver.find_element_by_xpath("//span[text()='立即投保']").click()
        # browser.find_element_by_xpath("//*[contains(text(),'花呗')]").click()
        # driver.find_element_by_xpath("//div[text()='本人']")
        time.sleep(2)

    finally:
        driver.quit()

def test_iyunbao():
    pass