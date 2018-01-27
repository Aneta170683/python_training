# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application2 import Application2


@pytest.fixture
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy2)
    return fixture


def test_add_contact(app):
    app.session_contact.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Anna", lastname="Test", title="kontakt", company="Testowa", address="Polna 1", mobile="111222333", email="test1@wp.pl"))
    app.session_contact.logout()

def test_add_empty_contact(app):
    app.session_contact.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", lastname="", title="", company="", address="", mobile="", email=""))
    app.session_contact.logout()

