#!/usr/bin/python

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker

fake = Faker()
password = 'EvilC0rp$$$'
#acctNum = int(input('[+] How many bots would you like to make today? '))
sep = '@'


def proxyGen():
    # Pull IP from proxy_file, or scrape a new proxy with proxyReq.py if none exists
    try:
        f = open('proxy_file.txt','r')
        os.system('python proxyReq.py')
        global proxy_ip
        proxy_ip = f.read()
        f.close()
        if len(proxy_ip) <= 1: # Checks if valid IP
            # Requests proxy
            os.system('python proxyReq.py')
    except:
        print("Warning: Proxy Not Activated")


def acctGen():
    randNum = fake.random_number()
    if randNum <= 2:
        randNum += randNum
    fullName = fake.name()
    firstName = fake.first_name()
    emailFake = fullName.replace(" ","") + str(randNum) + '@yandex.com'
    #print('[-] Generating '+ str(acctNum) + ' accounts..\nUser: ' + fullName + '\nEmail: ' + emailFake + '\nPassword: ' + password)
    # Increase this sleep time (in seconds) if it isn't filling out data
    sleep(5)
    # Find and iterate through input form
    inputs = browser.find_elements_by_xpath('//form/div/div/div/input')
    ActionChains(browser)\
        .move_to_element(inputs[0])\
        .click()\
        .send_keys(emailFake)\
        .move_to_element(inputs[1])\
        .click()\
        .send_keys(fullName)\
        .move_to_element(inputs[2])\
        .click()\
        .send_keys(emailFake.split(sep, 1)[0])\
        .move_to_element(inputs[3])\
        .click()\
        .send_keys(password)\
        .perform()

    # Click Sign Up button
    signUp = browser.find_element_by_xpath('//div/span/button')
    ActionChains(browser).move_to_element(signUp).click().perform()

    # Add profile photo
    profilebtn = browser.find_element_by_xpath('//button')
    profilebtn.send_keys(os.getcwd() + "images/1.png")
    sleep(10)


#def scrapePhoto():


#def addPhoto():


# Login Function Goes Here
def logIn():
    # Click Login Button
    login_elem = browser.find_element_by_xpath('//article/div/div/p/a[text()="Log in"]')
    ActionChains(browser).move_to_element(login_elem).click().perform()


def checkUsername():
    if username != 'X':
        write(r, 'database.xls')


if __name__ == '__main__':
    proxyGen()
    user_agent = 'Instagram 10.26.0 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)'
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument('--proxy-server=%s' % proxy_ip)
    # Paste chromedriver.exe to the root of your C drive if on Winblows
    browser = webdriver.Chrome('c:/chromedriver', chrome_options=options)
    browser.get('http://www.whatismyip.com')
    sleep(5)
    browser.get('https://www.instagram.com')
    for i in range(1):
        acctGen()
        #browser.refresh()
        #sleep(.5)

    #browser.close()
