from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app):
    contact_id = '167'
    group_id = '233'
    app.contact.add_contact_to_group(contact_id, group_id)
    contact = db.get_contact_in_group(group_id=group_id, contact_id=contact_id)
    assert contact_id == contact.id
    contacts_in_group = app.contact.get_contact_list()
    contact_ui = Contact(id=0)
    for c in contacts_in_group:
        if c.id == contact.id:
            contact_ui = c
            break
    assert contact == contact_ui