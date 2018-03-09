import re
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


# def test_phones_on_home_page(app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     # do testu z użyciem weryfikacji wstecznej
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
#     #do testu bez weryfikacji wstecznej czyli normalna asercja - porównuję to co jest na stronie głównej kontaktów
#     # z tym co jest w polu edycji - musze dodać do class jeśli nie mam lastname, firstname, address,
#     # musze dodąć w metodzie get contact list  oraz w metodzie get contact info from edit page
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#     assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#     assert contact_from_home_page.address == contact_from_edit_page.address

def test_all_contacts(app):
    contacts = app.contact.get_contact_list()
    cl = len(contacts)
    i = 0
    for c in contacts:
        contact_from_home_page = contacts[i]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(i)
        contact_from_view_page = app.contact.get_contact_from_view_page(i)
        contact_db = db.get_contact(contact=c)

        # do testu z użyciem weryfikacji wstecznej
        assert contact_from_home_page.all_phones_from_home_page == \
               merge_phones_like_on_home_page(contact_from_edit_page)
        assert contact_from_home_page.all_emails_from_home_page == \
               merge_emails_like_on_home_page(contact_from_edit_page)
        assert contact_from_home_page.lastname == contact_from_edit_page.lastname
        assert contact_from_home_page.firstname == contact_from_edit_page.firstname
        assert contact_from_home_page.address == contact_from_edit_page.address
        # tutaj asercja z bazki
        assert contact_from_home_page.lastname == xstr(contact_db.lastname)
        assert contact_from_home_page.firstname == xstr(contact_db.firstname)
        assert contact_from_home_page.address == xstr(contact_db.address)
        # porównywanie page info
        assert contact_from_view_page.homephone == contact_from_edit_page.homephone
        assert contact_from_view_page.workphone == contact_from_edit_page.workphone
        assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
        assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
        if i < cl-1:
            i += 1

# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#     assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def xstr(s):
    return '' if s is None else s

def clear(s):
    return re.sub("[() -]", "", s)

#weryfikacja wsteczna z użyciem lambda
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone,  contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))

#weryfikacja wsteczna z użyciem lambda
def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email,  contact.email2, contact.email3]))))
