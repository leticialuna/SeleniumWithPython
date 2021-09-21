from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\rodri\\Downloads\\driver\\chromedriver_win32\\chromedriver")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

# 1 - Scroll down pages by pixes
driver.execute_script("window.scrollBy(0,1000)", "")

# 2 - Scroll the page until the element is visible
flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[26]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();", flag)

# 3 - Scroll down page until end
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
