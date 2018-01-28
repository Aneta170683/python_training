

def test_delete_first_contact(app):
    app.session_contact.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session_contact.logout()
