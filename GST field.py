select_obj = Select(country_dropdown)
select_obj.select_by_value("India")

country_dropdown = driver.find_element("xpath", '(//input[@id="country-select-rhf-country-select-country"])[1]').click()
country_dropdown.send_keys("India")
country_dropdown.send_keys(Keys.ENTER)
sleep(4)
