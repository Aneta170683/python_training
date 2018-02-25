#from model.contact import Contact
import pytest
from data.add_contact import constant as testdata


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
        old_contacts = app.contact.get_contact_list()
        app.contact.create(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()



#def test_add_empty_contact(app):
    #old_contacts = app.contact.get_contact_list()
    #app.contact.create(Contact(firstname="", lastname="", title="", company="", address="", mobile="", email=""))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)



#testdata = [
        #Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 15),
                #title=random_string("title", 20), company=random_string("company", 10),
                #address=random_string("address", 20),
                #mobilephone=random_string("mobilephone", 10), email=random_string("email", 20)),
        #Contact(firstname="", lastname="", title="", company="", address="", mobilephone="", email="")
#]




#testdata = [
    #Contact(firstname=firstname, lastname=lastname,
            #title=title, company=random_string("company", 10),
            #address=random_string("address", 20),
            #mobilephone=random_string("mobilephone", 10), email=random_string("email", 20))
    #for firstname in ["", random_string("firstname", 10)]
    #for lastname in ["", random_string("lastname", 15)]
    #for title in ["", random_string("title", 20)]

#]


