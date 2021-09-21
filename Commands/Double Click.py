from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\rodri\\Downloads\\driver\\chromedriver_win32\\chromedriver")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)

actions.double_click(element).perform() #mouse double click
time.sleep(5)

#actions.context_click('variable').perform() #mouse right click

driver.close()
