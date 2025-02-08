from selenium import webdriver
# getting the chrome driver path 4 11
from selenium.webdriver.chrome.service import Service
# ln  to find elements on the web by names, id, xpath etc. 6
from selenium.webdriver.common.by import By


import time

from selenium.webdriver.support.select import Select

service = Service(executable_path="C:\\Browserdrivers\\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()

radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radio_buttons))
for buttons in radio_buttons:
    if buttons.get_attribute("value") == "radio3":
        buttons.click()
        assert buttons.is_selected()
        break

driver.find_element(By.ID, "autocomplete").send_keys("Ca")
time.sleep(2)
dropdown1 = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")
print(len(dropdown1))
for country in dropdown1:
    if country.text == "Canada":
        country.click()
        break

dropdown2 = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown2.select_by_index(3)



checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("id") == "checkBoxOption2":
        checkbox.click()
        assert checkbox.is_selected()
    elif checkbox.get_attribute("id") == "checkBoxOption1":
        checkbox.click()
        assert checkbox.is_selected()
    elif checkbox.get_attribute("id") == "checkBoxOption3":
        checkbox.click()

time.sleep(2)
driver.quit()