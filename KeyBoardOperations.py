from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = Chrome()
driver.get("http://www.theTestingWorld.com/testings")

driver.find_element(by='name', value='fld_username').send_keys('username')

act = ActionChains(driver)

# Perform tab key
# act.send_keys(Keys.TAB).perform()

# perform control + a (select text action)
act.key_down(Keys.CONTROL).send_keys('a').perform()

time.sleep(10)
