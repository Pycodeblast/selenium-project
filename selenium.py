#1) to open python website and search pycon
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.python.org")
sleep(4)
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
# elem = driver.find_element(By.ID,"id-search-field")
# elem = driver.find_element(By.XPATH,"//input[@id='id-search-field']")
# elem = driver.find_element(By.TAG_NAME, "input")
# elem = driver.find_element(By.CLASS_NAME, "search-field")
# elem = driver.find_element(By.CSS_SELECTOR, "input.search-field")#by tag.classname
# elem = driver.find_element(By.CSS_SELECTOR, "input#id-search-field")
elem.clear()
elem.send_keys("pycon")
# elem.send_keys(" pycon", Keys.ARROW_DOWN)
sleep(4)
elem.send_keys(Keys.RETURN)
sleep(4)
assert "No results found." not in driver.page_source
sleep(4)
driver.close()

# 2) login form
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.google.com")
sleep(4)
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("sample login")
sleep(4)
elem.send_keys(Keys.RETURN)
sleep(4)
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a/h3").click()
sleep(4)
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
sleep(4)
driver.find_element(By.NAME, "password").send_keys("1234")
sleep(4)
driver.find_element(By.XPATH,"/html/body/div/div/form/div[1]/div[3]").click()
sleep(4)

# 3) alert box
from selenium import webdriver
from selenium.webdriver.common.by import By
# class selenium.webdriver.common.alert.Alert(driver)
from selenium.webdriver.common.alert import Alert
from time import sleep
driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
sleep(4)
driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button').click()
sleep(4)
# Alert(driver).accept()
Alert(driver).dismiss()

# 4) screen shot
from selenium import webdriver
driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
driver.get('http://www.python.org/')
driver.save_screenshot('screenshot.png')
driver.quit()


# 5) scroll down
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
driver.get('http://www.python.org/')
sleep(4)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")