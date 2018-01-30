# -*- coding: utf-8 -*-

import pytest
from grupa import Grupa
from aplikacja import Aplikacja


@pytest.fixture
def ap(request):
    fixture = Aplikacja()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_dodanie_grupy(ap):
    ap.logowanie(username="admin", password="secret")
    ap.stworzenie_grupy(Grupa(name="testowanie", header="testy1", footer="testy2"))
    ap.wylogowanie()


def test_dodanie_pustej_grupy(ap):
    ap.logowanie(username="admin", password="secret")
    ap.stworzenie_grupy(Grupa(name="", header="", footer=""))
    ap.wylogowanie()

