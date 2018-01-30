# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from grupa import Grupa
from aplikacja import Aplikacja

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_dodanie_grupy(unittest.TestCase):
    def setUp(self):
        self.ap = Aplikacja()
    
    def test_dodanie_grupy(self):
        self.ap.logowanie(username="admin", password="secret")
        self.ap.stworzenie_grupy(Grupa(name="testowanie", header="testy1", footer="testy2"))
        self.ap.wylogowanie()


    def test_dodanie_pustej_grupy(self):
        self.ap.logowanie(username="admin", password="secret")
        self.ap.stworzenie_grupy(Grupa(name="", header="", footer=""))
        self.ap.wylogowanie()



    def tearDown(self):
        self.ap.destroy()

if __name__ == '__main__':
    unittest.main()
