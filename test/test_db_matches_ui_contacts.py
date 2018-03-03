
from test import test_phones
from model.contact import Contact

def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        all_emails = test_phones.merge_emails_like_on_home_page(contact)
        all_phones = test_phones.merge_phones_like_on_home_page(contact)

        firstname = contact.firstname.strip()

        lastname = contact.lastname.strip()
        if len(contact.lastname.strip()) == 0:
            lastname = None

        address = contact.address.replace("\r", "")
        if len(contact.address.strip()) == 0:
            address = None

        return Contact(id=contact.id,
                       firstname=firstname,
                       lastname=lastname,
                       address=address,
                       all_phones_from_home_page=all_phones,
                       all_emails_from_home_page=all_emails)
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
