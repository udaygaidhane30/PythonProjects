from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = r"C:\Users\Asus\Downloads\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)


driver.get("https://www.instagram.com/")

time.sleep(5)

username = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
username.send_keys("___you_day___")

password = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys("thisismypassword")

time.sleep(1)
login_button = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
login_button.click()

time.sleep(7)
search_bar = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
search_bar.send_keys("purvesh")
search_bar.send_keys(Keys.ENTER)
search_bar.send_keys(Keys.ENTER)