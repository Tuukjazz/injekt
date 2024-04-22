from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        project_data = toml.loads(content)
        project_data = project_data.get("tool").get("poetry")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        project = Project(
            project_data.get("name",[]),
            project_data.get("description",[]),
            project_data.get("authors",[]),
            project_data.get("license",[]),
            project_data.get("dependencies",[]),
            project_data.get("group").get("dev").get("dependencies",[])
        )
        return project
        
        