from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://mango-flower-081830400-stage.eastasia.5.azurestaticapps.net/")
driver.maximize_window()
sleep(2)

driver.find_element("xpath", '//button[text()="Sign in"]').click()
sleep(3)

driver.find_element("id", ":r21:").send_keys("8072255389")
sleep(2)

driver.find_element("id", ":r22:").click()
sleep(20)

driver.find_element("xpath", '//button[text()="Sign In"]').click()
sleep(5)

driver.find_element("xpath", '//div[@class="MuiBox-root css-1qou0sd"]').click()
sleep(3)

driver.find_element("xpath", '//span[@class="MuiBox-root css-d0uhtl"]').click()
sleep(2)

driver.find_element("xpath", '(//span[@class="MuiTypography-root MuiTypography-overline css-srcusa"])[1]').click()
sleep(2)

company_name = "Poo"
company_name_field = driver.find_element("xpath", '//input[@id=":r23:"]').send_keys(company_name)
sleep(2)

def validate_name(company_name_field):
   
    name_regex = r'^[A-Za-z]+([ ]?[A-Za-z]+)*$'
    
    if not company_name_field or company_name_field.strip() == "":
        return "Name field is empty."
    
    if len(company_name_field.strip()) < 4:
        return "Name must be at least 4 characters long."
    
    if not re.match(name_regex, company_name_field.strip()):
         return "Invalid name. Only letters and spaces are allowed."

    else:
        return "Valid Name."

print(validate_name(company_name))


