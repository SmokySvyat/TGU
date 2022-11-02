import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.alert import Alert

s=Service('E://Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)

#Let's delete pasport
driver.get("https://adminqa.neapro.site/login")
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='admin_email']").send_keys("moderat@neapro.ru")
driver.find_element(By.XPATH, "//*[@id='admin_password']").send_keys("Aa123456")
driver.find_element(By.XPATH, "//*[@id='admin_submit_action']/input").click()
driver.find_element(By.XPATH, "//*[@id='students']/a").click()
driver.find_element(By.XPATH, "//*[@id='users']/a").click()
driver.execute_script("document.getElementsByClassName('sidebar')[0].click()")
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='q_second_name']").send_keys("Питонский")
driver.find_element(By.XPATH, "//*[@id='new_q']/div[9]/input[1]").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#user_2387 > td.col.col-actions > div > a.view_link.member_link").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

driver.find_element(By.LINK_TEXT, "Удалить").click()
alert = driver.switch_to.alert
alert.accept()

