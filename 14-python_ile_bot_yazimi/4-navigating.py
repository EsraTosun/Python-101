from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By   # sayfada istediğimiz bölmü bulmamızı sağlar
import time

driver = webdriver.Chrome()

url ="http://github.com"
driver.get(url)


searchInput = driver.find_element(By.XPATH ,"//*[@id='query-builder-test']")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
# result = driver.page_source
result = driver.find_elements(By.CSS_SELECTOR,".repo-list-item h3 a")

for element in result:
    print(element.text)

driver.close()