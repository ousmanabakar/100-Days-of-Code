from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PASSWORD = "2345"
EMAIL = "test"
PROMISED_DOWNLOAD = 130
PROMISED_UPLOAD = 50
CHROME_DRIVER_PATH = "/home/ousman/Development/chromedriver_linux64/chromedriver"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def get_internet_speed(self):
        self.driver.set_window_size(640, 480)
        self.driver.get("https://fast.com/")
        sleep(30)
        go_button = self.driver.find_element_by_id('show-more-details-link')
        go_button.click()
        sleep(30)
        self.down = self.driver.find_element_by_xpath('//*[@id="speed-value"]').text
        self.up = self.driver.find_element_by_xpath('//*[@id="upload-value"]').text
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.set_window_size(640, 480)
        self.driver.get("https://twitter.com/login")
        self.driver.implicitly_wait(10)

        # Set up your email infos
        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div['
            '2]/div/input'
        )
        email.send_keys(EMAIL)
        sleep(10)
        email.send_keys(Keys.ENTER)
        sleep(10)

        # Set up your password infos
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div['
            '2]/div/input'
        )
        sleep(2)
        password.send_keys(PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)
        sleep(10)

        # Text area for to tweet
        tweet_area = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div['
            '2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
        )
        tweet_area.send_keys(f"Hey internet provider why my internet speed is {self.down}Mbps download/{self.up}Mbps "
                             f"upload instead of {PROMISED_DOWNLOAD}Mbps/{PROMISED_UPLOAD}Mbps")

        # Click to the tweet button
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div['
            '2]/div[3]/div/div/div[2]/div[3]/div/span/span'
        )
        tweet_button.click()

        sleep(10)
        print("successfully completed")
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
