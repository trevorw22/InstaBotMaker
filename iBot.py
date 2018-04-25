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
acctNum = int(input('[+] How many bots would you like to make today? '))
sep = '@'


def acctGen():
    randNum = fake.random_number()
    if randNum != 3:
        randNum += randNum
    fullName = fake.name()
    firstName = fake.first_name()
    emailFake = fullName.replace(" ","") + str(randNum) + '@mail.com'
    print('[-] Generating '+ str(acctNum) + ' accounts..\nUser: ' + fullName + '\nEmail: ' + emailFake + '\nPassword: ' + password)

    #Increase the sleep time (in seconds) if it isn't filling out data in the sign up forms
    sleep(.5)

    #email_elem = browser.find_element_by_name('emailOrPhone')
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
    print(i)
    signUp = browser.find_element_by_xpath('//div/span/button')
    #ActionChains(browser).move_to_element(signUp).click().perform()
    #sleep(5)

#Login Function Goes Here
#login_elem = browser.find_element_by_xpath('//article/div/div/p/a[text()="Log in"]')
#ActionChains(browser).move_to_element(login_elem).click().perform()

#sleep(5)
#browser.close()

if __name__ == '__main__':
    for i in acctNum:
        browser = webdriver.Chrome('c:\chromedriver')
        browser.get('https://www.instagram.com')
        acctGen()
        browser.refresh()
        sleep(.5)
