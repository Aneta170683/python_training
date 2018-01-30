# -*- coding: utf-8 -*-
import pytest
from model.kontakt import Kontakt
from fixture.aplikacja import Aplikacja



@pytest.fixture
def ap(request):
    fixture = Aplikacja()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_dodanie_kontaktu(ap):
    ap.sesja.logowanie(username="admin", password="secret")
    ap.kontakty.stworzenie(Kontakt(firstname="Anna", lastname="Kwiatek", address="Wiejska 2", home="111222111"))
    ap.sesja.wylogowanie()

def test_dodanie_pustego_kontaktu(ap):
    ap.sesja.logowanie(username="admin", password="secret")
    ap.kontakty.stworzenie(Kontakt(firstname="", lastname="", address="", home=""))
    ap.sesja.wylogowanie()
