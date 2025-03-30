import time


from selenium import webdriver
# getting the chrome driver path 4 11
from selenium.webdriver.chrome.service import Service
# ln  to find elements on the web by names, id, xpath etc. 6
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


service = Service(executable_path="C:\\Browserdrivers\\chromedriver.exe")


driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)


driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(2)
number_of_items = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(number_of_items)
assert count == 3
print(len(number_of_items))


actual_list = []
product_name = driver.find_elements(By.XPATH, "//div[@class='product']/h4")
for products in product_name:
    actual_list.append(products.text)
print(actual_list)


for result in number_of_items:
    result.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[.='PROCEED TO CHECKOUT']").click()

# Sum validation
sum_of_items = driver.find_elements(By.XPATH, "//tr/td[5]/p")
added_sum = 0
for items in sum_of_items:
    added_sum = added_sum + int(items.text)


total_amount = len(sum_of_items)
print(added_sum)
assert added_sum == 388
print(total_amount)


driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()


wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)


discount_amt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert discount_amt < added_sum








