from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys

driver = Chrome()
driver.get("http://www.theTestingWorld.com/")

act = ActionChains(driver)

# Perform click operation anywhere on page
# act.click().perform()

# Perform click operation on specified element on page
# act.click(driver.find_element(by='xpath', value="//a[@id='menu516']")).perform()

# Perform Context-click (right click) operation anywhere on page
# act.context_click().perform()
# act.context_click(driver.find_element(by='xpath', value="//a[@id='menu516']")).perform()

# Setting control (mouse hover)
act.move_to_element(driver.find_element(by='xpath', value="//a[@id='menu577']")).perform()

# input('Wait')
