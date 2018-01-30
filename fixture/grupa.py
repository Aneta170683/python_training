class GrupaPomoc:

    def __init__(self,ap):
        self.ap = ap

    def powrot_na_strone_z_grupami(self):
        wd = self.ap.wd
        wd.find_element_by_link_text("group page").click()

    def usuniecie_pierwszej_grupy(self):
        wd = self.ap.wd
        self.otwarcie_strony_z_grupami()
        # wybieramy pierwsza grupe
        wd.find_element_by_name("selected[]").click()
        # usuwamy pierwsza grupe
        wd.find_element_by_name("delete").click()
        self.powrot_na_strone_z_grupami()

    def stworzenie(self, grupa):
        wd = self.ap.wd
        self.otwarcie_strony_z_grupami()
        # wybranie karty dodania grupy
        wd.find_element_by_name("new").click()
        # wypełnienie karty z grupa
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(grupa.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(grupa.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(grupa.footer)
        # potwierdzenie dodania grupy
        wd.find_element_by_name("submit").click()
        self.powrot_na_strone_z_grupami()

    def otwarcie_strony_z_grupami(self):
        wd = self.ap.wd
        wd.find_element_by_link_text("groups").click()
