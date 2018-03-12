from fixture.orm import ORMFixture
from model.contact import Contact

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_delete_contact_from_group(app, check_ui):
    contact_id = '167'
    group_id = '233'
    app.contact.delete_contact_from_group(contact_id, group_id)
    contact = db.get_contact_in_group(group_id=group_id, contact_id=contact_id)
    assert contact.id == -1
    contacts_in_group = app.contact.get_contact_list()
    contact_ui = None
    for c in contacts_in_group:
        if c.id == contact_id:
            contact_ui = c
            break
    assert contact_ui == None