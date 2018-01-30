class KontaktPomoc:

    def __init__(self,ap):
        self.ap = ap

    def stworzenie(self, Kontakt):
        wd = self.ap.wd
        self.otwarcie_strony_z_kontaktami()
        # stworzenie kontaktu
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Kontakt.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Kontakt.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Kontakt.address)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Kontakt.home)
        # potwierdzenie dodania kontaktu
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def otwarcie_strony_z_kontaktami(self):
        wd = self.ap.wd
        wd.find_element_by_link_text("add new").click()