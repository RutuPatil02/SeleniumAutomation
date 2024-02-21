from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time


# path="C:\\Users\\shara\\Downloads\\chromedriver_win32.exe"
# driver = Chrome(executable_path=path)

driver = Chrome()
driver.get("http://www.thetestingworld.com/testings")

driver.maximize_window()

driver.find_element(by='name', value='fld_username').send_keys('username')
driver.find_element(by='xpath', value="//input[@name='fld_email']").send_keys('username@gmail.com')
driver.find_element(by='name', value='fld_password').send_keys('abcd123')

driver.find_element(by='name', value='fld_cpassword').send_keys('abcd123')
driver.find_element(by='name', value='add_type').send_keys('xyz')
driver.find_element(by='name', value='phone').send_keys('123456789')

# work on radio button
driver.find_element(by='xpath', value="//input[@value='home']").click()

# work on Dropdown
obj = Select(driver.find_element(by='name', value='sex'))
obj.select_by_index(1)

obj2 = Select(driver.find_element(by='name', value='country'))
obj2.select_by_value('101')

# obj3 = Select(driver.find_element(by='name', value='state'))
# obj3.select_by_value('22')

# work on sign-up button
driver.find_element(by='xpath', value="//input[@type='submit']").click()

# work on link
driver.find_element(by='link text', value='Read Detail').click()

# input('Plz wait')

time.sleep(100)

# driver.close()
