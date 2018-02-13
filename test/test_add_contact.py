# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Anna", lastname="Test", title="kontakt", company="Testowa", address="Polna 1",
                               mobile="111222333", email="test1@wp.pl"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)




def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", title="", company="", address="", mobile="", email=""))

