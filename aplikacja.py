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

    def destroy(self):
        self.wd.quit()
