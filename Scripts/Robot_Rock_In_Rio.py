from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\rodri\\Downloads\\driver\\chromedriver_win32\\chromedriver")

driver.get("https://rockinrio.com/rio/pt-br/home/")
driver.maximize_window()
driver.find_element_by_link_text("LINE-UP").click()
time.sleep(2)
driver.find_element_by_id("btn-dias").click()
time.sleep(2)

elements = driver.find_elements_by_xpath("//*[@id='collapseDias']/div/a")

links = []
for el in elements:
    links.append((el.get_attribute('href'), el.text))

for l in links:
    driver.get(l[0])
    time.sleep(1)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "dest-1"))
        )
        for i in element:
            print("Dia ", l[1], i.text)
    except:
        print("Dia ", l[1], " Nao ha artistas confirmados")
        
