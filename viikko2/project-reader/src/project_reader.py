import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # toml to dict
        content_toml = toml.loads(content)
        poetry_dict = content_toml['tool']['poetry']
        name = poetry_dict['name']
        desc = poetry_dict['description']
        deps = list(poetry_dict['dependencies'])
        dev_deps = list(poetry_dict['dev-dependencies'])
        return Project(name, desc, deps, dev_deps)
