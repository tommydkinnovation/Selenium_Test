from selenium import webdriver
# object of ChromeOptions class
o = webdriver.ChromeOptions()
# adding Chrome Profile Path
o.add_argument = {'user-data-dir': '/Users/Application/Chrome/Default'}
# set chromedriver.exe path
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", options=o)
# maximize browser
driver.maximize_window()
# launch URL
driver.get("https://www.tutorialspoint.com/index.htm")
# get browser title
print(driver.title)
# quit browser
driver.quit()
