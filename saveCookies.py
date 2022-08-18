# save cookies

import pickle
import selenium.webdriver

driver = selenium.webdriver.Chrome()
driver.get("http://www.youtube.com")
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
