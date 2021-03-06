from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, id=None, title=None, company=None, address=None, homephone= None,
                 workphone=None, mobilephone=None, secondaryphone = None, all_phones_from_home_page=None,  email=None,
                 email2=None, email3=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page




    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.title, self.company,
                                            self.address, self.mobilephone, self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
                and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize





