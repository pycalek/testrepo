from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "D:/PROGRAMS/chromedriver.exe"
url = "https://tinder.com/app/recs"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)
login_button = driver.find_element_by_xpath('//*[@id="t-429325247"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()
time.sleep(1)
facebook_login = driver.find_element_by_xpath('//*[@id="t--1610880557"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
facebook_login.click()
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
email_entry = driver.find_element_by_xpath('//*[@id="email"]')
password_entry = driver.find_element_by_xpath('//*[@id="pass"]')
email_entry.send_keys("pycalkowaty@gmail.com")
password_entry.send_keys("1&&NHYv)^pcO")
zaloguj = driver.find_element_by_class_name("uiButtonConfirm")
zaloguj.click()
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)
location = driver.find_element_by_xpath('//*[@id="t--1610880557"]/div/div/div/div/div[3]/button[1]')
location.click()
time.sleep(2)
powiadomienia = driver.find_element_by_xpath('//*[@id="t--1610880557"]/div/div/div/div/div[3]/button[2]')
try:
    powiadomienia.cilck()
except:
    powiadomienia.send_keys(Keys.TAB)
    powiadomienia.send_keys(Keys.TAB)
    powiadomienia.send_keys(Keys.ENTER)
coockies = driver.find_element_by_xpath('//*[@id="t-429325247"]/div/div[2]/div/div/div[1]/button')
coockies.click()
keep_swiping = True
while keep_swiping:
    try:
        like_her = driver.find_element_by_xpath('//*[@id="t-429325247"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_her.click()
        time.sleep(2)
    except:
        like_her.send_keys(Keys.TAB)
        #time.sleep(1)
        like_her.send_keys(Keys.ENTER)



