from selenium import webdriver
# getting the chrome driver path 4 11
from selenium.webdriver.chrome.service import Service
# ln  to find elements on the web by names, id, xpath etc. 6
from selenium.webdriver.common.by import By


name = "Lekan"


service = Service(executable_path="C:\\Browserdrivers\\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@class='inputs']").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert name in alert_text
alert.accept()