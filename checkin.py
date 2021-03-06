#!/usr/bin/env python
'''
Checkin script
'''

import time
import random

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

HIDE_UI = True


def main():
    '''
    main function
    '''

    account = '<account>'
    password = '<password>'
    config_url = ''

    if config_url != '':
        r = requests.get(config_url)
        conf = r.json()
        if ('checkin' not in conf) or (not conf['checkin']):
            print('No checkin today')
            return

    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument('--no-sandbox')

    if HIDE_UI:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

    rand_start = random.randint(0, 300)

    print('Start after {} seconds...'.format(rand_start))
    time.sleep(rand_start)

    print('Open login page...')
    chrome.get(
        "https://scsservices.azurewebsites.net/Login.aspx?CompanyID=QYD547AA59Z53H3CCC27552C"
    )

    print('Do login...')
    accountInput = chrome.find_element_by_id('edtUserID_I')
    passwordInput = chrome.find_element_by_id('edtPassword_I')
    login = chrome.find_element_by_id('btnLogin')

    accountInput.send_keys(account)
    passwordInput.send_keys(password)
    login.click()

    time.sleep(3)

    print('Navigate to checkin page...')
    chrome.get('https://scsservices.azurewebsites.net/HRM/ATT/AttEmpOnlineSwipe.aspx')

    time.sleep(3)

    print('Do checking...')
    checkin = chrome.find_element_by_id('btnOnSwipe')
    checkin.click()

    time.sleep(3)
    print('Done')

if __name__ == '__main__':
    main()
