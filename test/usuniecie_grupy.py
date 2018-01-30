


def test_usuniecie_pierwszej_grupy(ap):
    ap.sesja.logowanie(username="admin", password="secret")
    ap.grupa.usuniecie_pierwszej_grupy
    ap.sesja.wylogowanie()