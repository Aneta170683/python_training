# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from kontakt import Kontakt

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_dodanie_kontaktu(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files/Mozilla Firefox ESR/firefox.exe")
        self.wd.implicitly_wait(60)
    
    def test_dodanie_kontaktu(self):
        wd = self.wd

        self.otwarcie_strony_home_page(wd)
        self.logowanie(wd, username="admin", password="secret")
        self.otwarcie_strony_z_kontaktami(wd)
        self.stworzenie_kontaktu(wd, Kontakt(firstname="Anna", lastname="Kwiatek", address="Wiejska 2", home="111222111"))
        self.wylogowanie(wd)

    def test_dodanie_pustego_kontaktu(self):
        wd = self.wd

        self.otwarcie_strony_home_page(wd)
        self.logowanie(wd, username="admin", password="secret")
        self.otwarcie_strony_z_kontaktami(wd)
        self.stworzenie_kontaktu(wd, Kontakt(firstname="", lastname="", address="", home=""))
        self.wylogowanie(wd)

    def wylogowanie(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def stworzenie_kontaktu(self, wd, Kontakt):
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

    def otwarcie_strony_z_kontaktami(self, wd):
        wd.find_element_by_link_text("add new").click()

    def logowanie(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def otwarcie_strony_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
