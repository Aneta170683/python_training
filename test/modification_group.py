

def test_modification_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_group(group_name="testowanie", group_header="testowanie2", group_footer="testowanie3")
    app.session.logout()