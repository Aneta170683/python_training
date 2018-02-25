
from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname1", lastname="lastname1",
            title="title1", company="company1", address="addres1", mobilephone="mobilephone1", email="email1"),
    Contact(firstname="firstname2", lastname="lastname2",
            title="title2", company="company2", address="addres2", mobilephone="mobilephone2", email="email2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", title="", company="", address="", mobilephone="", email="")] + [
        Contact(firstname=random_string("firstname", 10),
                lastname=random_string("lastname", 15),
                title=random_string("title", 20),
                company=random_string("company", 10),
                address=random_string("address", 20),
                mobilephone=random_string("mobile", 10),
                email=random_string("email", 20))
        for i in range(3)
]