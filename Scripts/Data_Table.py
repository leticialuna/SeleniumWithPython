from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\rodri\\Downloads\\driver\\chromedriver_win32\\chromedriver")

driver.get("file:///C:/Users/rodri/Desktop/seleniumpractice.html")

linhas = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr")) #conta o numero de linhas
colunas = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th")) #conta o numero de colunas

print("Quantidade de ", linhas)
print("Quantidade de ", colunas)
print("Product", "  ", "Article","  ", "Price")

for l in range(2, linhas+1):
    for c in range(1, colunas+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(l)+"]/td["+str(c)+"]").text
        print(value, end='    ')
    print()
