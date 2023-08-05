from selenium import webdriver
import time   # ziyaret ettiğimiz sayfada durmamızı sağlar

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)   # girdiğimiz url ziyaret eder

time.sleep(2)    # url de 2 sn durur
driver.maximize_window()   # yüklendikten 2 sn sonra tam ekran olur
driver.save_screenshot("github.com-homepage.png")
# Açtığı sayfanın ekran görüntüsü alır

url = "http://github.com/EsraTosun"
driver.get(url)

print(driver.title)

if "EsraTosun" in driver.title: 
     driver.save_screenshot("github-EsraTosun.png")

time.sleep(2)

driver.back()   # sayfayı geri alır
# driver.forward()  # sayfayı ileri alır

time.sleep(2)

driver.close()
