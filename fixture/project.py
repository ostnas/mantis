from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def open_manage_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def open_create_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_create_page.php")):
            self.open_manage_projects_page()
            wd.find_element_by_xpath("//input[@value='Create New Project']").click()


    def fill_project_form(self, project):
        wd = self.app.wd
        self.app.fill_text_field("name", project.name)
        self.app.fill_text_field("description", project.description)

    def create_project(self, project):
        wd = self.app.wd
        self.open_create_project_page()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def delete_project_by_index(self, index):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_elements_by_css_selector("td > a[href*='manage_proj_edit_page.php?project_id']")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    def get_project_list(self):
        wd = self.app.wd
        self.open_manage_projects_page()
        project_list = []
        for project in wd.find_elements_by_css_selector("td > a[href*='manage_proj_edit_page.php?project_id']"):
            id = project.get_attribute('search').split('=')[1]
            name = project.text
            project_list.append(Project(name=name, id=id))
        return project_list

