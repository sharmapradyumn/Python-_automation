from selenium import webdriver
from selenium.webdriver.common.by import By

baseUrl = "https://www.w3schools.com/html/html_tables.asp"
driver = webdriver.Firefox(executable_path="D:\\Soft\\Jars\\geckodriver-v0.23.0-win64\\geckodriver.exe")
driver.get(baseUrl)
allElements = driver.find_elements(By.XPATH, "//div[@class='w3-example']//tbody//tr")
length = len(allElements)
print("length of str " + str(length))

print(allElements.__sizeof__())
driver.close()