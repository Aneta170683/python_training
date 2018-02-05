# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Anna", lastname="Test", title="kontakt", company="Testowa", address="Polna 1",
                               mobile="111222333", email="test1@wp.pl"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", title="", company="", address="", mobile="", email=""))

