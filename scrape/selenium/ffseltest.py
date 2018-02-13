
# Import your newly installed selenium package
from selenium import webdriver

# Now create an 'instance' of your driver
# This path should be to wherever you downloaded the driver
driver = webdriver.Chrome(executable_path="./chromedriver")
###driver = webdriver.Firefox(executable_path="./geckodriver")
# A new Chrome (or other browser) window should open up

'''
chromedriver (google chrome)
geckodriver (firefox & mozilla/opera)
microsoftwebdriver (windows only)
''' and None

# Now just tell it wherever you want it to go
driver.get("https://medium.com/@dalewahl")

'''
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://seleniumhq.org/')
''' and None
