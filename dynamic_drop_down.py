
from selenium import webdriver
# getting the chrome driver path 4 11
from selenium.webdriver.chrome.service import Service
# ln  to find elements on the web by names, id, xpath  6
from selenium.webdriver.common.by import By


import time



service = Service(executable_path="C:\\Browserdrivers\\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/dropdownsPractise")
driver.maximize_window()
driver.find_element(By.ID, "autosuggest").send_keys("Can")
time.sleep(5)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class*='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "Canada":
        country.click()
        break

#Using the 'get_attribute' to select text from a dynamic dropdown
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Canada"


time.sleep(5)




driver.quit()