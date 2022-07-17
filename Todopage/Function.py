from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time
import random
import string
import inspect


class Function(object):
    PATH = "D:\\Automation\\Todopage\\chromedriver.exe"
    github_link = By.XPATH, "//span[@class='fa fa-github']"
    chrome_link = By.XPATH, "//div/a[1]"

    username = By.ID,  "login_field"
    password = By.ID,  "password"
    signin_button = By.XPATH, "//input[@type='submit' and @name='commit']"

    github_authority = By.ID, "js-oauth-authorize-btn"

    addlist_button = By.XPATH, "//button[@class='btn btn-success btn-block glyphicon glyphicon-plus task-btn']"
    text_list = By.XPATH, "//div[@class='row']/div/input[1]"
    logoff_button = By.XPATH,   "//button[@class='btn btn-default']"

    def __init__(self):
        self.driver = None
        self.wait = None

    def open_web_browser(self, url):
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(url)
            self.driver.maximize_window()
            self.wait = WebDriverWait(self.driver, 20)
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='fa fa-github']")))
        except:
            raise AssertionError(inspect.stack()[0][3] + " ...Open web browser fail" + '\n\n\n')

    def close_web_browser(self):
        try:
            if self.driver is not None:
                self.driver.close()
                self.driver.quit()
        except:
            raise AssertionError(inspect.stack()[0][3] + " ...Close web broswer failed" + '\n\n\n')

    def login_with_github(self, username_github, password_github):
        try:
            window = self.driver.current_window_handle
            self.driver.find_element(*self.github_link).click()
            for window1 in self.driver.window_handles:
                if window1 != window:
                    self.driver.switch_to.window(window1)
                    break

            self.wait.until(EC.presence_of_element_located((By.ID, 'login_field')))
            self.driver.find_element(*self.username).send_keys(username_github)
            self.driver.find_element(*self.password).send_keys(password_github)
            self.driver.find_element(*self.signin_button).click()
            try:
                self.wait.until(EC.presence_of_element_located((By.ID, 'js-oauth-authorize-btn')))
                self.driver.find_element(*self.github_authority).click()
            except:
                print("don't need authority")
        except:
            raise AssertionError(inspect.stack()[0][3] + " ...Log in with github fail" + '\n\n\n')

    def logout_to_do_page(self):
        try:
            self.driver.find_element(*self.logoff_button).click()
        except:
            raise AssertionError(inspect.stack()[0][3] + " ...Log out fail" + '\n\n\n')

    def randomword(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def create_list_to_do_on_web_browser(self):
        try:
            for window in self.driver.window_handles:
                    self.driver.switch_to.window(window)
                    break
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='row']/div/input[1]")))

            for i in range(10):
                self.driver.find_element(*self.text_list).send_keys(self.randomword(10))
                self.driver.find_element(*self.addlist_button).click()
            time.sleep(3)
        except:
            raise AssertionError(inspect.stack()[0][3] + " ...Create list fail" + '\n\n\n')

    def delete_list_to_do_from_5_to_10_on_web_browser(self):
        try:
            for window in self.driver.window_handles:
                self.driver.switch_to.window(window)
                break
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//ul[@class='list-group']/li[1]/div/div[2]/button")))

            for i in range(10, 1, -1):
                if i > 5:
                    delete = By.XPATH, "//ul[@class='list-group']/li[" + str(i) + "]/div/div[2]/button"
                    time.sleep(1)
                    self.driver.find_element(*delete).click()
        except:
            raise AssertionError(inspect.stack()[0][3] + " ...Delete list fail" + '\n\n\n')


    def delete_all_list(self):
        try:
            for window in self.driver.window_handles:
                self.driver.switch_to.window(window)
                break
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//ul[@class='list-group']/li[1]/div/div[2]/button")))

            time.sleep(1)

            for i in range(20):
                element = self.driver.find_element(*(By.XPATH, "//ul[@class='list-group']/li[1]/div/div[2]/button"))
                if element != 0:
                    time.sleep(1)
                    element.click()
        except:
            print("Don't have any list")

