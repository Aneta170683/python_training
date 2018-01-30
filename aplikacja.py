from selenium.webdriver.firefox.webdriver import WebDriver

class Aplikacja:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files/Mozilla Firefox ESR/firefox.exe")
        self.wd.implicitly_wait(60)

    def wylogowanie(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def powrot_na_strone_z_grupami(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def stworzenie_grupy(self, grupa):
        wd = self.wd
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
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def logowanie(self, username, password):
        wd = self.wd
        self.otwarcie_strony_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def otwarcie_strony_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def wylogowanie(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def stworzenie_kontaktu(self, Kontakt):
        wd = self.wd
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
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def logowanie(self, username, password):
        wd = self.wd
        self.otwarcie_strony_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def otwarcie_strony_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
    def destroy(self):
        self.wd.quit()
