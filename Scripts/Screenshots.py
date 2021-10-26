from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\rodri\\Downloads\\chromedriver_win32\\chromedriver")

driver.get("https://www.amazon.com.br/")

#Choose the format
driver.save_screenshot("C:\\Users\\rodri\\Downloads\\homepage.png")

#Salve in jpg
driver.get_screenshot_as_file("C:\\Users\\rodri\\Downloads\\homepage2")
