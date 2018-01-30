class SesjaPomoc:

    def __init__(self,ap):
        self.ap = ap



    def logowanie(self, username, password):
            wd = self.ap.wd
            self.ap.otwarcie_strony_home_page()
            wd.find_element_by_name("user").click()
            wd.find_element_by_name("user").clear()
            wd.find_element_by_name("user").send_keys(username)
            wd.find_element_by_name("pass").click()
            wd.find_element_by_name("pass").click()
            wd.find_element_by_name("pass").clear()
            wd.find_element_by_name("pass").send_keys(password)
            wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def wylogowanie(self):
            wd = self.ap.wd
            wd.find_element_by_link_text("Logout").click()
