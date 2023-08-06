from githubUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By   # sayfada istediğimiz bölmü bulmamızı sağlar
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/input[2]").send_keys(self.username)
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[1]").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[13]").click()

    def loadFollowers(self):
        items = self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed")

        for i in items:
            self.followers.append(i.find_element(By.CSS_SELECTOR,".f4.Link--primary").text)


    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)

        self.loadFollowers()

        while True:
            links = self.browser.find_element(By.CLASS_NAME,"BtnGroup").find_elements_by_tag_name("a")

            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadFollowers()

                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)
                        self.loadFollowers()
                    else:
                        continue


github = Github(username, password)
github.signIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)

