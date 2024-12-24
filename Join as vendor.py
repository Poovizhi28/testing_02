from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import re

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://mango-flower-081830400-stage.eastasia.5.azurestaticapps.net/")
driver.maximize_window()
sleep(5)

driver.find_element("xpath", '//button[text()="Join as Vendor"]').click()
sleep(3)

company_name = "Poovizhi"
company_name_field = driver.find_element("xpath", '//input[@id=":r1q:"]').send_keys(company_name)
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
company_email_field = driver.find_element("xpath", '//input[@id=":r1r:"]').send_keys(company_email)
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

phone_number = "8072255389"
phone_number_field = driver.find_element("xpath", '//input[@id=":r1s:"]').send_keys(phone_number)
sleep(2)

def validate_phone_number(phone_number_field):
    phone_regex = r'^[0-9]{10}$'
    
    if not phone_number_field or phone_number_field.strip() == "":
        return "Phone number field is empty."
    
    if not re.match(phone_regex, phone_number_field.strip()):
         return "Invalid phone number. It should be 10 digits."

    else:
        return "Valid Phone Number."

print(validate_phone_number(phone_number))

driver.find_element("xpath", '//input[@name="termsAndConditions"]').click()
sleep(2)

driver.find_element("xpath", '//button[@id=":r1t:"]').click()
sleep(2)

OTP_field = driver.find_element("xpath", '//input[@id=":r1u:"]').click()
sleep(10)

sign_as_vendor = driver.find_element("xpath", '//button[@id=":r24:"]').click()
sleep(10)

profile_icon = driver.find_element("xpath", '//div[@class="MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-wutwh6"]').click()
sleep(10)

profile_button = driver.find_element("xpath", '//span[text()="Profile"]').click()
sleep(2)

company_info_button = driver.find_element("xpath", '//span[@class="MuiTypography-root MuiTypography-overline css-srcusa"][1]').click()
sleep(2)

scroll_down = driver.execute_script("window.scrollBy(0, 250);")
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
sleep(6)

def validate_email(company_email):
   
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if not company_email or company_email.strip() == "":
        return "Email address field is empty."
    
    if not re.match(email_regex, company_email.strip()):
         return "Invalid Email ID."

    else:
        return "Valid Email ID."

print(validate_email(company_email))


# phone_number_field = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//input[@id=":r37:"]'))
# )
# phone_number = "8072255389"
# phone_number_field.send_keys(phone_number)
# sleep(6)

# def validate_phone_number(phone_number):
#     phone_regex = r'^[0-9]{10}$'
    
#     if not phone_number or phone_number.strip() == "":
#         return "Phone number field is empty."
    
#     if not re.match(phone_regex, phone_number.strip()):
#          return "Invalid phone number. It should be 10 digits."

#     else:
#         return "Valid Phone Number."

# print(validate_phone_number(phone_number))

# gst_number1 = "22AAAAA0000A1Z5"
# gst_number = driver.find_element("xpath", '//input[@id=":r38:"]').send_keys(gst_number1)
# sleep(6)

# def validate_gst(gst_number):
   
#     gst_regex = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$'
    
#     if not gst_number or gst_number.strip() == "":
#         return "GST Number field is empty."
    
#     if re.match(gst_regex, gst_number):
#         return "Valid GST Number"
#     else:
#         return "Invalid GST Number"


# print(validate_gst(gst_number1))

# address1 = "4/223, gandhipuram, coimbatore, Tamil Nadu, India"
# address = driver.find_element("xpath", '//input[@id=":r39:"]').send_keys(address1)
# sleep(6)

# def validate_address(address):
#     if len(address.strip()) < 50:
#         return "Address must be at least 50 characters long."
#     else:
#         return "Valid address."

# print (validate_address(address1))


select_country = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '(//input[@id="country-select-rhf-country-select-country"])[1]'))
)
select_country.send_keys("India")
select_country.send_keys(Keys.RETURN)
sleep(3)


select_city = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(("xpath", '(//input[@id="rhf-autocomplete-city"])[1]'))
)
select_city.send_keys("Option 1")
select_city.send_keys(Keys.RETURN)
sleep(4) 


select_state = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(("xpath", '(//input[@id="rhf-autocomplete-state"])[1]'))
)
select_state.send_keys("Option 1")
select_state.send_keys(Keys.RETURN)
sleep(4)

zipcode1 = "65421"
zipcode = driver.find_element("xpath", '//input[@id=":r3g:"]').send_keys(zipcode1)
sleep(4)

zipcode_pattern = r"^\d{6}$"

def validate_zipcode(zipcode):
    zipcode_pattern = r"^\d{6}$"

    if re.match(zipcode_pattern, zipcode):
        print("Valid Zipcode")
    else:
        print("Invalid Zipcode")

print (validate_zipcode(zipcode1))

update_comp_info = driver.find_element("xpath", '//button[@id=":r2h:"]').click()
sleep(2)















update_profile = driver.find_element("xpath", '//button[@id=":r26:"]').click()
sleep(2)



