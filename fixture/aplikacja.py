from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sesja import SesjaPomoc
from fixture.grupa import GrupaPomoc

class Aplikacja:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files/Mozilla Firefox ESR/firefox.exe")
        self.wd.implicitly_wait(60)
        self.sesja = SesjaPomoc(self)
        self.grupa = GrupaPomoc(self)


    def otwarcie_strony_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")


    def stworzenie_kontaktu(self, Kontakt):
        wd = self.wd
        self.otwarcie_strony_z_kontaktami()
        # stworzenie kontaktu
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Kontakt.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Kontakt.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Kontakt.address)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Kontakt.home)
        # potwierdzenie dodania kontaktu
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def otwarcie_strony_z_kontaktami(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()


    def otwarcie_strony_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
    def destroy(self):
        self.wd.quit()
