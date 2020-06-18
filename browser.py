from selenium import webdriver
from selenium.webdriver.common.by import By

class browserintraction():

    def browsermethod(self):

        baseUrl = "https://www.seleniumhq.org/"
        driver = webdriver.Firefox(executable_path="D:\\Soft\\Jars\\geckodriver-v0.23.0-win64\\geckodriver.exe")
        driver.get(baseUrl)
        #to maximize window
        driver.maximize_window()
        print("Window maxmize Done")

        title = driver.title
        print("Title of the web page is: " + title)

        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        # Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")

        # Open another Url
        driver.get(baseUrl)
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)
        # Browser Back
        driver.back()
        print("Go one step back in browser history")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)
        # Browser Forward
        driver.forward()
        print("Go one step forward in browser history")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)
        # Get Page Source
        pageSource = driver.page_source
        print(pageSource)


        driver.close()

obj = browserintraction()
obj.browsermethod()