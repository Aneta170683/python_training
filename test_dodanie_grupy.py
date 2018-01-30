# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from grupa import Grupa

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_dodanie_grupy(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files/Mozilla Firefox ESR/firefox.exe")
        self.wd.implicitly_wait(60)
    
    def test_dodanie_grupy(self):
        wd = self.wd
        self.otwarcie_strony_home_page(wd)
        self.logowanie(wd, username="admin", password="secret")
        self.otwarcie_strony_z_grupami(wd)
        self.stworzenie_grupy(wd, Grupa(name="testowanie", header="testy1", footer="testy2"))
        self.powrot_na_strone_z_grupami(wd)
        self.wylogowanie(wd)


    def test_dodanie_pustej_grupy(self):
        wd = self.wd
        self.logowanie(wd, username="admin", password="secret")
        self.stworzenie_grupy(wd, Grupa(name="", header="", footer=""))
        self.wylogowanie(wd)

    def wylogowanie(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def powrot_na_strone_z_grupami(self, wd):
        wd.find_element_by_link_text("group page").click()

    def stworzenie_grupy(self, wd, grupa):
        self.otwarcie_strony_z_grupami(wd)
        # wybranie karty dodania grupy
        wd.find_element_by_name("new").click()
        # wypełnienie karty z grupa
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(grupa.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(grupa.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(grupa.footer)
        # potwierdzenie dodania grupy
        wd.find_element_by_name("submit").click()
        self.powrot_na_strone_z_grupami(wd)

    def otwarcie_strony_z_grupami(self, wd):
        wd.find_element_by_link_text("groups").click()

    def logowanie(self, wd, username, password):
        self.otwarcie_strony_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def otwarcie_strony_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
