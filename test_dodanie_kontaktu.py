# -*- coding: utf-8 -*-
import pytest
from kontakt import Kontakt
from aplikacja import Aplikacja



@pytest.fixture
def ap(request):
    fixture = Aplikacja()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_dodanie_kontaktu(ap):
    ap.logowanie(username="admin", password="secret")
    ap.stworzenie_kontaktu(Kontakt(firstname="Anna", lastname="Kwiatek", address="Wiejska 2", home="111222111"))
    ap.wylogowanie()

def test_dodanie_pustego_kontaktu(ap):
    ap.logowanie(username="admin", password="secret")
    ap.stworzenie_kontaktu(Kontakt(firstname="", lastname="", address="", home=""))
    ap.wylogowanie()
