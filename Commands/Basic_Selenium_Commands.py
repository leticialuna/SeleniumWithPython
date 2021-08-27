from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\rodri\\Downloads\\driver\\chromedriver_win32\\chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")

# Get the title
print(driver.title)

#Get the Current Url
print(driver.current_url)

#Click in the element
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)

#Close the element - only on page at a time
driver.close() 

#Close all the browser
driver.quit() 

# Implicit Wait - When you want to wait, but not the complete time as sleep. If the page load before the estimate time, the remaing time will be discarted
driver.implicitly_wait(5)

# Explicit Wait
# Using the library time, it is possible to use sleep for wait the time you want
time.sleep (5)

#Using Expected Conditions with the library `from selenium.webdriver.support import expected_conditions AS EC`
wait=WebDriveWait(driver, 5)
element = wait.until(EC.element_to_be_clickable((By.XPATH,"codigo")))
