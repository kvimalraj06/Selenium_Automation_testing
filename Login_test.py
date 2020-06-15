from selenium import webdriver
import time

class LoginTests():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def baseurl(self, url):
        self.base_url = url
        self.driver.get(self.base_url)


    def login_check(self, username, password):

        self.username = username
        self.username_field = self.driver.find_element_by_id("username")
        self.username_field.clear()
        self.username_field.send_keys(self.username)

        self.password = password
        self.pass_field = self.driver.find_element_by_id("password")
        self.pass_field.send_keys(self.password)

        self.login_button = self.driver.find_element_by_xpath("/html/body/div[2]/div/main/div/form/h5[2]/div[2]/button")
        self.login_button.click()

        try:
            self.login_check = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[2]/a")
            print("login Successfull")
            self.login = True
        except:
            print("login not successful")
            self.login = False


    def login_logout(self, username, password):
        careconnect.login_check(username, password)
        if self.login == True:
            self.logout_button = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[9]/a")
            time.sleep(5)
            self.logout_button.click()
            print("logged out successfully")
            #self.driver.quit()
        else:
            print("can't log out because of unsuccessful login")
            #self.driver.quit()

    def repeat(self, count):
        for i in range(3):
            user_name_bar = self.driver.find_element_by_id("username")
            pass_field = self.driver.find_element_by_id("password")
            login_button = self.driver.find_element_by_xpath("/html/body/div[2]/div/main/div/form/h5[2]/div[2]/button")
            user_name_bar.clear()
            user_name_bar.send_keys("username")
            pass_field.send_keys("password")
            login_button.click()
            logout_button = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[9]/a")
            time.sleep(5)
            logout_button.click()


careconnect = LoginTests()
careconnect.baseurl('https://dev-india.careconnectclinic.com')
careconnect.login_logout("username","password")