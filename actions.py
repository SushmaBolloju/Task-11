

import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

paths = r"C:\Users\chand\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options=Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(3)
# open the window using given url
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
time.sleep(3)

# Switch to the frame containing the draggable elements
driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="content"]/iframe'))

# Find the draggable element
draggable_element = driver.find_element(By.ID,'draggable')
print(draggable_element.text)

# Find the droppable element
droppable_element = driver.find_element(By.ID, 'droppable')

# perform drag and drop action
actions = ActionChains(driver)
actions.drag_and_drop(draggable_element, droppable_element).perform()

# check if drag and drop action is successful
if "Dropped!" in droppable_element.text:
    print("Drag and drop successful!")
else:
    print("Drag and drop failed.")

time.sleep(5)
driver.quit()
