from time import sleep
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

TARGETED_ACCOUNT = ""
PASSWORD = "password"
EMAIL = "username"

CHROME_DRIVER_PATH = "/home/ousman/Development/chromedriver_linux64/chromedriver"


class InstaFollower:
    def __init__(self, chrome_path):
        self.driver = webdriver.Chrome(executable_path=chrome_path)

    def login(self):
        # Get The URL
        self.driver.get("https://www.instagram.com")
        sleep(5)
        username_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_field.send_keys(EMAIL)

        password_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers(self):
        sleep(5)
        self.driver.get("https://www.instagram.com/chefsteps/")
        follower_list = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follower_list.click()
        sleep(5)

    def scroll_down(self):
        modal = self.driver.find_element_by_css_selector('.isgrP')
        sleep(15)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

    def follow(self):
        print("follow called")
        follow_button = self.driver.find_elements_by_css_selector('li button')
        for button in follow_button:
            sleep(2)
            if button.text == "Follow":
                print("followed")
                button.click()
            else:
                print("passed")
                pass
            self.scroll_down()


instaBot = InstaFollower(CHROME_DRIVER_PATH)
instaBot.login()
instaBot.find_followers()
instaBot.follow()
