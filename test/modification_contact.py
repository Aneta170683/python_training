
def test_modification_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modification_contact(middlename="Katarzyna", address="Polna 2", email="testy@wp.pl")
    app.session.logout()