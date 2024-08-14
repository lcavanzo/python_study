from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
# browser.get("https://inventwithpython.com") # for testing class_name and Link_text
browser.get("https://login.metafilter.com")  # for texting ID
try:
    # elem = browser.find_element(By.CLASS_NAME, "cover-thumb")
    # elem = browser.find_element(By.LINK_TEXT, "Read Online for Free")
    # elem.click()
    # print(f"Found <{elem.tag_name}> element with that class name!")
    user_elem = browser.find_element(By.ID, "user_name")
    user_elem.send_keys("link")
    pass_elem = browser.find_element(By.ID, "user_pass")
    pass_elem.send_keys("zelda")
    pass_elem.submit()

except:
    print("Wast not able to find an element with that name")
