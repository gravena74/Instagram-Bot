from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class InstaBot:
    def __init__(self, username, password) -> None:
        # Username
        self.username = username
        # Password
        self.password = password
        # Which browser will the driver use
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

    def login(self):
        driver = self.driver
        # Enter the site
        driver.get("http://www.instagram.com")
        # Time 5 seconds
        time.sleep(5)

        # Put the username in the login
        log = driver.find_element_by_name("username").send_keys(self.username)
        # Put the password in the login
        log = driver.find_element_by_name("password")
        log.send_keys(self.password)
        log.send_keys(Keys.RETURN)
        time.sleep(5)

        # Data
        driver.find_element(By.XPATH, '//button[text()="Not now"]').click()
        time.sleep(5)
        # notification 
        driver.find_element(By.XPATH, '//button[text()="Not now"]').click()
        time.sleep(5)

    def follows(self):
        driver = self.driver
        # Enter the See all
        driver.find_element_by_link_text('See all').click()
        time.sleep(5)

        # Infinite loop
        while True:
            # Repeat 2 times
            for i in range(2):
                # Repeat 10 times
                for k in range(10):
                    # Follow
                    driver.find_element(By.XPATH, '//button[text()="Follow"]').click()
                    # Time 2 seconds
                    time.sleep(2)
                # Repeat 10 times
                for j in range(10):
                    # If there are "Following" button
                    try: 
                        # Following
                        driver.find_element(By.XPATH, '//button[text()="Following"]').click()
                        time.sleep(2)
                        # Unfollow
                        driver.find_element(By.XPATH, '//button[text()="Unfollow"]').click()
                        time.sleep(2)
                    # If there are not "Following" button
                    except NoSuchElementException:
                        # Requested
                        driver.find_element(By.XPATH, '//button[text()="Requested"]').click()
                        time.sleep(2)
                        # Unfollow
                        driver.find_element(By.XPATH, '//button[text()="Unfollow"]').click()
                        time.sleep(2)

                # Refresh the page
                driver.refresh()
                time.sleep(5)
            # 2 hour time to no get blocked
            time.sleep(7200)


# Login: Username and Password
b = InstaBot('', '')
b.login()
b.follows()
