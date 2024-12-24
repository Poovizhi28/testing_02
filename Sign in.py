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
sleep(5)

driver.find_element("xpath", '//button[text()="Sign in"]').click()
sleep(3)

driver.find_element("id", ":r21:").send_keys("8072255389")
sleep(2)

driver.find_element("id", ":r22:").click()
sleep(8)

company_name = "Poovizhi"
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

company_email = "poovizhi@yahoo.com"
company_email_field = driver.find_element("xpath", '//input[@id=":r24:"]').send_keys(company_email)
sleep(2)

def validate_email(company_email):
   
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if not company_email or company_email.strip() == "":
        return "Email address field is empty."
    
    if not re.match(email_regex, company_email.strip()):
         return "Invalid Email ID."

    else:
        return "Valid Email ID."

print(validate_email(company_email))

driver.find_element("xpath", '//button[text()="Proceed"]').click()
sleep(4)

driver.find_element("xpath", '//input[@id=":r1q:"]').click()
sleep(10)

driver.find_element("xpath", '//button[@id=":r20:"]').click()
sleep(8)

# driver.find_element("xpath", '//button[text()="Sign In"]').click()
# sleep(5)

driver.find_element("xpath", '//div[@class="MuiBox-root css-1qou0sd"]').click()
sleep(3)

driver.find_element("xpath", '//span[@class="MuiBox-root css-d0uhtl"]').click()
sleep(2)

# Company information:

company_name = "Poovizhi"
company_name_field = driver.find_element("xpath", '//input[@id=":r25:"]').send_keys(company_name)
sleep(4)

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

company_email = "poovizhi@yahoo.com"
company_email_field = driver.find_element("xpath", '//input[@id=":r26:"]').send_keys(company_email)
sleep(4)

def validate_email(company_email):
   
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if not company_email or company_email.strip() == "":
        return "Email address field is empty."
    
    if not re.match(email_regex, company_email.strip()):
         return "Invalid Email ID."

    else:
        return "Valid Email ID."

print(validate_email(company_email))

phone_number = "8072255389"
phone_number_field = driver.find_element("xpath", '//input[@id=":r27:"]').send_keys(phone_number)
sleep(4)

def validate_phone_number(phone_number_field):
    phone_regex = r'^[0-9]{10}$'
    
    if not phone_number_field or phone_number_field.strip() == "":
        return "Phone number field is empty."
    
    if not re.match(phone_regex, phone_number_field.strip()):
         return "Invalid phone number. It should be 10 digits."

    else:
        return "Valid Phone Number."

print(validate_phone_number(phone_number))

update_profile = driver.find_element("xpath", '//button[@id=":r28:"]').click()
sleep(2)
































# gst_number1 = "22AAAAA0000A1Z5"
# gst_number = driver.find_element("xpath", '//input[@id=":r26:"]').send_keys(gst_number1)
# sleep(2)

# def validate_gst(gst_number):
   
#     gst_regex = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$'
    
#     if not gst_number or gst_number.strip() == "":
#         return "GST Number field is empty."
    
#     if re.match(gst_regex, gst_number):
#         return "Valid GST Number"
#     else:
#         return "Invalid GST Number"


# print(validate_gst(gst_number1))

# pan_number1 = "NPWPS8343W"
# pan_number = driver.find_element("xpath", '//input[@id=":r27:"]').send_keys(pan_number1)
# sleep(2)

# def validate_pan(pan_number):
   
#     pan_regex = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    
#     if not pan_number or pan_number.strip() == "":
#         return "PAN Number field is empty."
    
#     if re.match(pan_regex, pan_number):
#         return "Valid PAN Number"
#     else:
#         return "Invalid PAN Number"

# print(validate_pan(pan_number1))

# address1 = "4/223, gandhipuram, coimbatore, Tamil Nadu, India"
# address = driver.find_element("xpath", '//textarea[@id=":r28:"]').send_keys(address1)

# def validate_address(address):
#     if len(address.strip()) < 50:
#         return "Address must be at least 50 characters long."
#     else:
#         return "Valid address."

# print (validate_address(address1))

# driver.find_element("xpath", '//button[@id=":r29:"]').click()