from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\rodri\\Downloads\\driver\\chromedriver_win32\\chromedriver")

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_element_list = []
boxes_city = ["box%d" % x for x in range(1, 8)]
for el in boxes_city:
    source_element_list.append(driver.find_element_by_id(el))

target_element_list = []
boxes_country = ["box10%d" % x for x in range(1, 8)]
for el in boxes_country:
    target_element_list.append(driver.find_element_by_id(el))

dict_elements = dict(zip(source_element_list, target_element_list))

for key, value in dict_elements.items():
    ActionChains(driver).drag_and_drop(key, value).perform()
    
driver.close()
