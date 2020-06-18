from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWindow():

    def test(self):
        baseUrl = "https://www.seleniumhq.org/"
        driver = webdriver.Firefox(executable_path="D:\\Soft\\Jars\\geckodriver-v0.23.0-win64\\geckodriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                time.sleep(2)
                searchBox = driver.find_element(By.ID, "search-courses")
                searchBox.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        # Switch back to the parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, "name").send_keys("Test Successful")
        driver.quit()



ff = SwitchToWindow()
ff.test()