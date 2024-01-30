import random
import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

fake = Faker()

driver: WebDriver = webdriver.Chrome()
driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")
driver.maximize_window()

print("Filling up form")
driver.implicitly_wait(1)
print("Fill up name and last name")

first = driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]")
first.clear()
first.send_keys(fake.first_name())
time.sleep(1)

last = driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[2]")
last.clear()
last.send_keys(fake.last_name())
time.sleep(1)

print("Fill up email")
email = driver.find_element(By.XPATH, "//input[contains(@type,'email')]")
email.clear()
email.send_keys(fake.email())
time.sleep(1)

print("Fill up phone number")

telephone = driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[2]/div[3]/div[1]/div[1]/input[1]")
telephone.clear()
telephone.send_keys(fake.phone_number())
time.sleep(1)

print("Select product")
RundomNumber = random.randint(0, 5)
driver.find_element(By.ID, "radio-0000000e" + str(RundomNumber)).click()
time.sleep(1)

print("Fill up Quantity")
random_Quantity = driver.find_element(By.XPATH,
                                      "/html[1]/body[1]/form[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/input[1]")
random_Quantity.clear()
random_Quantity.send_keys(random.randint(0, 10))
time.sleep(1)

print("Select date")
driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[1]/div[2]").click()
driver.find_element(By.XPATH, "//html//body//div//div//div//div//div[contains(text(),'10')]").click()
time.sleep(1)

print("Fill up address")
address = driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[2]/div[7]/div[1]/div[1]/input[1]")
address.clear()
address.send_keys(fake.address())
time.sleep(1)

city = driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[2]/div[7]/div[1]/div[3]/input[1]")
city.clear()
city.send_keys(fake.city())
time.sleep(1)

state = driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[2]/div[7]/div[1]/div[3]/input[2]")
state.clear()
state.send_keys(fake.state())
time.sleep(1)

zip_cod = driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[2]/div[7]/div[1]/div[4]/input[1]")
zip_cod.clear()
zip_cod.send_keys(random.randint(0, 99999))
time.sleep(1)

print("Select from Coutry dropdown")

driver.find_element(By.XPATH, "//input[@placeholder='Country']").send_keys('Canada')
time.sleep(1)

print("Select from Dropdown dropdown")

RundomNumberA = random.randint(0, 2)
Select(driver.find_element(By.TAG_NAME, 'select')).select_by_index(RundomNumberA)

driver.execute_script(f"window.scrollTo(0, {2 ** 127});")
time.sleep(2)
print("Select checkbox Multiple choice")
RundomNumber3 = random.randint(1, 3)
print(RundomNumber3)
driver.find_element(By.XPATH, "//body[1]/form[1]/div[1]/div[2]/div[9]/div[1]/div[" + str(
    RundomNumber3) + "]/div[1]/label[1]/span[1]").click()

time.sleep(1)

print("Submitting form")

submit = driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[4]/div[2]/div[1]/button[1]/span[1]")
body = driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[4]/div[2]/div[1]/button[1]/span[1]")
if submit:
    submit.click()
elif driver.body.send_keys(Keys.PAGE_DOWN):
    submit.click()

driver.close()
