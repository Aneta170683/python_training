from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session_contact import SessionContactHelper
from fixture.contact import ContactHelper


class Application2:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files/Mozilla Firefox ESR/firefox.exe")
        self.wd.implicitly_wait(60)
        self.session_contact = SessionContactHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy2(self):
        self.wd.quit()
