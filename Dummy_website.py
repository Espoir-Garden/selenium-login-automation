
from selenium import webdriver
# getting the chrome driver path 4 11
from selenium.webdriver.chrome.service import Service
# ln  to find elements on the web by names, id, xpath etc 6
from selenium.webdriver.common.by import By
# to interact with buttons or keys on the actual keyboard 8
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

import time

from selenium.webdriver.support.select import Select

service = Service(executable_path="C:\\Browserdrivers\\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
driver.find_element(By.NAME, "name").send_keys("Olamilekan Akinsulire")
time.sleep(5)
driver.find_element(By.NAME, "email").send_keys("olamilekan@example.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345qwerty")
time.sleep(5)
driver.find_element(By.ID, "exampleCheck1").click()
# The code below handles static dropdown on the website from ln 28 - 34
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)
time.sleep(4)
dropdown.select_by_visible_text("Female")
time.sleep(4)
dropdown.select_by_visible_text("Male")

# driver.find_element(By.ID, "exampleFormControlSelect1").send_keys("Male")
driver.find_element(By.CLASS_NAME, "form-check-input").click()
driver.find_element(By.NAME, "bday").send_keys("09/29/1999")
driver.find_element(By.XPATH, "//input[@class = 'btn btn-success']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@class='ng-untouched ng-pristine ng-valid']").clear()

time.sleep(5)
message = driver.find_element(By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']").text
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("HIGH GARDEN")
print(message)
assert "Success" in message


title = driver.title
url = driver.current_url
print(title, url)
time.sleep(10)
driver.quit()