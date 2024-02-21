from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time


driver = Chrome()
driver.get("http://www.thetestingworld.com/testings")

driver.maximize_window()

print(driver.title)
print(driver.current_url)

# driver.find_element(by='class name',value='displayPopup').text

# Fetch element text
print("Text on link is = " + driver.find_element(by='class name', value='displayPopup').text)

# Fetch attribute value of element
print("Value of button is = " + driver.find_element(by='xpath', value='//input[@type="submit"]').get_attribute('value'))

# Fetch options from dropdown
obj = Select(driver.find_element(by='name', value='sex'))
obj.select_by_visible_text('Male')

for v in obj.options:
    print(v.text)

time.sleep(10)

# input('wait')
