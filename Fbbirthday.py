#Facebook Birthday Wisher
#CREATED BY AVINASH RAI
#ver 1.0
#just you have to run this python Script
#Don't know how to run go to readme.txt

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.keys import Keys 
import time 
  
chrome_options = webdriver.ChromeOptions() 
  
prefs = {"profile.default_content_setting_values.notifications": 2} 
chrome_options.add_experimental_option("prefs", prefs)
#download chromedrive extension from website "https://chromedriver.chromium.org/" and give the link of chromedrive.exe here
browser = webdriver.Chrome("C:\\Users\\Downloads\\Compressed\\chromedriver_win32_2\\chromedriver.exe") 
  
# open facebook.com using get() method 
browser.get('https://www.facebook.com/') 

# enter user_name or e-mail id
username = "avinash.rai147@gmail.com"
# create a password file somewhere in your pc and copy link here with "\\"   
with open('C:\\Users\\pass.txt', 'r') as myfile: 
    password = myfile.read().replace('\n', '') 
print("Let's Begin") 
  
element = browser.find_elements_by_xpath('//*[@id ="email"]')
element[0].send_keys(username) 
  
print("Username Entered") 
  
element = browser.find_element_by_xpath('//*[@id ="pass"]')
element.send_keys(password) 
  
print("Password Entered")
  
# logging in 
log_in = browser.find_elements_by_id('loginbutton')
log_in[0].click() 
  
print("Login Successfull") 
  
browser.get('https://www.facebook.com/events/birthdays/')
  
feed = 'Happy Birthday !'
  
element = browser.find_elements_by_xpath("//*[@class ='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")
cnt = 0
  
for el in element: 
    cnt += 1
    element_id = str(el.get_attribute('id'))
    XPATH = '//*[@id ="' + element_id + '"]'
    post_field = browser.find_element_by_xpath(XPATH) 
    post_field.send_keys(feed) 
    post_field.send_keys(Keys.RETURN) 
    print("Birthday Wish posted for friend" + str(cnt))
browser.close()
