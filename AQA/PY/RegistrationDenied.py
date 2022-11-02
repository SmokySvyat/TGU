import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service('E://Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)

##########################################
#           Open site Bumbleby           #
##########################################

driver.get("https://qa.neapro.site/login")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("pytests@yopmail.com")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("12345678")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)

##########################################
#               Fill Pasport             #
##########################################

driver.find_element(By.CSS_SELECTOR, ".active .document-tile:nth-child(1)").click()
driver.find_element(By.ID, "surname").clear()
driver.find_element(By.ID, "surname").send_keys("Питонский")
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").send_keys("Тест")
driver.find_element(By.ID, "patronymic").clear()
driver.find_element(By.ID, "patronymic").send_keys("Тестович")
driver.find_element(By.ID, "passportSeries").clear()
driver.find_element(By.ID, "passportSeries").send_keys("8888")
driver.find_element(By.ID, "passportNumber").clear()
driver.find_element(By.ID, "passportNumber").send_keys("148869")
driver.find_element(By.CSS_SELECTOR, "#birthday > div > input").send_keys("18.11.1993")
driver.find_element(By.XPATH, "//*[@id='dateOfIssue']/div/input").click()
driver.find_element(By.XPATH, "//*[@id='dateOfIssue']/div/input").send_keys("23.11.2013")
driver.find_element(By.ID, "code").click()
driver.find_element(By.ID, "code").clear()
driver.find_element(By.ID, "code").send_keys("540112")
driver.find_element(By.ID, "cardId").click()
driver.find_element(By.ID, "cardId").clear()
driver.find_element(By.ID, "cardId").send_keys("45612398745")
driver.find_element(By.XPATH, "//*[@id='issued']").clear()
driver.find_element(By.XPATH, "//*[@id='issued']").send_keys("Пастафариане")
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").clear()
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").send_keys("г Новосибирск, ул Тюленина, д 1")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__suggestions-item").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='phone']").click()
driver.find_element(By.XPATH, "//*[@id='phone']").clear()
driver.find_element(By.XPATH, "//*[@id='phone']").send_keys("9996661312")

#########    Download and Send  ##########

driver.find_element(By.XPATH, "//input[@type='file']").send_keys("D:\Работы\CARCASSONNE.png")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".fill").click()

##########################################
#         Let's delete pasport           #
##########################################

driver.get("https://adminqa.neapro.site/login")
driver.find_element(By.XPATH, "//*[@id='admin_email']").send_keys("moderat@neapro.ru")
driver.find_element(By.XPATH, "//*[@id='admin_password']").send_keys("Aa123456")
driver.find_element(By.XPATH, "//*[@id='admin_submit_action']/input").click()
driver.find_element(By.XPATH, "//*[@id='students']/a").click()

#########       Find User       ##########

driver.find_element(By.XPATH, "//*[@id='users']/a").click()
driver.execute_script("document.getElementsByClassName('sidebar')[0].click()")
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='q_second_name']").send_keys("Питонский")
driver.find_element(By.XPATH, "//*[@id='new_q']/div[9]/input[1]").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#user_2387 > td.col.col-actions > div > a.view_link.member_link").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

#########         Delete        ##########

driver.find_element(By.LINK_TEXT, "Удалить").click()
alert = driver.switch_to.alert
time.sleep(1)
alert.accept()
time.sleep(5)

driver.quit()