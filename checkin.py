#!/usr/bin/env python2
'''
Checkin script
'''

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SHOW_UI = False


def main():
    '''
    main function
    '''

    options = Options()
    options.add_argument("--disable-notifications")

    if SHOW_UI:
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')

    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome.get(
        "https://scsservices.azurewebsites.net/Login.aspx?CompanyID=QYD547AA59Z53H3CCC27552C"
    )

    account = chrome.find_element_by_id('edtUserID_I')
    password = chrome.find_element_by_id('edtPassword_I')
    login = chrome.find_element_by_id('btnLogin')

    account.send_keys('<account>')
    password.send_keys('<password>')
    login.click()

    time.sleep(3)

    chrome.get('https://scsservices.azurewebsites.net/HRM/ATT/AttEmpOnlineSwipe.aspx')

    time.sleep(3)

    checkin = chrome.find_element_by_id('btnOnSwipe')
    checkin.click()

    time.sleep(5)

if __name__ == '__main__':
    main()
