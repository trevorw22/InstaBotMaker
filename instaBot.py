from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

# The following variables and for loop will change once we get the list of identities loaded, or choose a way to automate identity generation....
randNum = 1337
firstName = []
for line in firstName:
    firstName = open(r, 'identityGen')


browser = webdriver.Chrome('c:\chromedriver')
browser.get('https://www.instagram.com')

sleep(.2)
#email_elem = browser.find_element_by_name('emailOrPhone')

inputs = browser.find_elements_by_xpath('//form/div/div/div/input')
ActionChains(browser).move_to_element(inputs[0]).click().send_keys('elliot_alderson@evilcorp.net').move_to_element(inputs[1]).click().send_keys('elliot alderson').move_to_element(inputs[2]).click().send_keys('elliot_alderson' + str(randNum)).move_to_element(inputs[3]).click().send_keys('EvilC0rp$$$').perform()

signUp = browser.find_element_by_xpath('//div/span/button')
ActionChains(browser).move_to_element(signUp).click().perform()


#Login
#login_elem = browser.find_element_by_xpath('//article/div/div/p/a[text()="Log in"]')
#ActionChains(browser).move_to_element(login_elem).click().perform()

#sleep(5)
#browser.close()
