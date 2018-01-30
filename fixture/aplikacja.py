from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sesja import SesjaPomoc
from fixture.grupa import GrupaPomoc
from fixture.kontakty import KontaktPomoc

class Aplikacja:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files/Mozilla Firefox ESR/firefox.exe")
        self.wd.implicitly_wait(60)
        self.sesja = SesjaPomoc(self)
        self.grupa = GrupaPomoc(self)
        self.kontakty = KontaktPomoc(self)

    def otwarcie_strony_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
