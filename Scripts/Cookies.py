from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\rodri\\Downloads\\chromedriver_win32\\chromedriver")

driver.get("https://www.amazon.in/")

#capture all the cookies

cookies = driver.get_cookies()
print(len(cookies)) #number of cookies
print(cookies) #print cookie pairs

#adding new cookie to the browser

cookie = {'name': 'mycookie', 'value': '12334567890'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies)) # after adding a new cookie
print(cookies) #print cookie pairs

# deleting cookie
driver.delete_cookie('mycookie')
cookies = driver.get_cookies()
print(len(cookies)) #after deleting the cookie
print(cookies) #print cookie pairs

#deleting all the cookies

driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))
