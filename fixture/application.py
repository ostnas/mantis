from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from selenium.webdriver.support.ui import Select


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/my_view_page.php")):
            wd.get(self.base_url)

    def fill_text_field(self, fieldname, value):
        wd = self.wd
        if value is not None:
            wd.find_element_by_name(fieldname).click()
            wd.find_element_by_name(fieldname).clear()
            wd.find_element_by_name(fieldname).send_keys(value)


    def destroy(self):
        self.wd.quit()