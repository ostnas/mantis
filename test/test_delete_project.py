from model.project import Project
from random import randrange

def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="new_project"))

    old_project_list = app.project.get_project_list()
    index = randrange(len(old_project_list))
    app.project.delete_project_by_index(index)
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) - 1 == len(new_project_list)
    old_project_list[index:index+1] = []
    assert old_project_list == new_project_list