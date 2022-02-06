from selenium import webdriver

driver_path = r"C:\Users\Asus\Downloads\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)

# driver.get("https://www.python.org/")
# time_data = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
#
# data_dict = {}
#
# for i in range(0,len(event_names)):
#     data_dict[i] = {"time":time_data[i].text, "name":event_names[i].text}
#
# print(data_dict)
# driver.close()

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname_input = driver.find_element_by_name("fName")
fname_input.send_keys("Uday")

lname_input = driver.find_element_by_name("lName")
lname_input.send_keys("Gaidhane")

email_id = driver.find_element_by_name("email")
email_id.send_keys("udaygaidhane@gmail.com")

signup_button = driver.find_element_by_css_selector("button")
signup_button.click()