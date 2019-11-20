from model.project import Project
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    app.session.login("administrator", "root")
    old_project_list = app.project.get_project_list()
    project = Project(name=random_string("name",10), description=random_string("description",15))
    app.project.create_project(project)
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) + 1 == len(new_project_list)
    old_project_list.append(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)