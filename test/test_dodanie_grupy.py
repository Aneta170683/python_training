# -*- coding: utf-8 -*-

import pytest
from model.grupa import Grupa
from fixture.aplikacja import Aplikacja


@pytest.fixture
def ap(request):
    fixture = Aplikacja()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_dodanie_grupy(ap):
    ap.sesja.logowanie(username="admin", password="secret")
    ap.stworzenie_grupy(Grupa(name="testowanie", header="testy1", footer="testy2"))
    ap.sesja.wylogowanie()


def test_dodanie_pustej_grupy(ap):
    ap.sesja.logowanie(username="admin", password="secret")
    ap.stworzenie_grupy(Grupa(name="", header="", footer=""))
    ap.sesja.wylogowanie()

