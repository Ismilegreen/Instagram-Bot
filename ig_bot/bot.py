
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randint
from pw import password
import emoji

PATH = "C:\Program Files (x86)\chromedriver.exe"


class InstaBot:
    links = []

    comments = ['So dope!','Bonkers','Geez','FUEGO!!', 'That looks awesome!!!', 'Excelente', 'SICK!!!!', 'JIGGY', 'WAVVVYYY MY FRIEND', 'YOU DID GOOD KID', 'ATTA BOY', 'Good look, Good look', 'Nice!!']

    def __init__(self):
        self.login('deuce_luse')
        self.like_comment_follow_by_hashtag('smile')
        # self.unfollow()
    

    def login(self, username):
        self.driver = webdriver.Chrome(PATH)
        self.username = username
        self.driver.get('https://www.instagram.com/')
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

    def like_comment_follow_by_hashtag(self, hashtag):
        search_box = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
        search_box.send_keys('#' + hashtag)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').send_keys(Keys.ENTER)
        sleep(5)

        links = self.driver.find_elements_by_tag_name('a')
        def condition(link):
            return '.com/p' in link.get_attribute('href')
        valid_links = list(filter(condition, links))

        for i in range(8):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in  self.links:
            self.driver.get(link)

            #like
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            sleep(3)

            #comment
            # self.driver.find_element_by_class_name('X7cDz').click()
            # sleep(1)
            # self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,12)])
            # sleep(2)
            # self.driver.find_element_by_xpath("//button[@type='submit']").click()
            # sleep(2)

            #follow
            self.driver.find_element_by_xpath("//button[@type='button']").click()
            sleep(2)

    def unfollow(self):
        self.driver.get('https://www.instagram.com/deuce_luse/')
        self.driver.find_element_by_partial_link_text('following').click()
        sleep(2)
    
        for i in range(40):
            self.driver.find_element_by_xpath("//button[contains(text(), 'Following')]").click()
            sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
            sleep(2)


def main():
    my_bot = InstaBot()

if __name__== '__main__':
    main()