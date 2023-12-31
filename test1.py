import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login = "standard_user"
password_all = "secret_sauce"

username = driver.find_element(By.XPATH,"//input[@id='user-name']")
username.send_keys(login)
print("Input Login")
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input password")
butonLogin = driver.find_element(By.XPATH,"//input[@id='login-button']")
butonLogin.click()
print("Click Login Button")
# textProducts = driver.find_element(By.XPATH,"//span[@class='title']")
# valueTextProducts = textProducts.text
# print(valueTextProducts)
# assert valueTextProducts == "Products"
# print("Good")

url = "https://www.saucedemo.com/inventory.html"
getUrl = driver.current_url
print(getUrl)
assert url == getUrl
print("OK URl")