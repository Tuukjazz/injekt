class Project:
    def __init__(self, name, description, authors, license, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.authors = authors
        self.license = license
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dictionery(self, dictionery):
        return "\n- " + "\n- ".join(dictionery) if len(dictionery) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n"
            f"\nAuthors: {self._stringify_dictionery(self.authors)}"
            f"\n"
            f"\nDependencies: {self._stringify_dictionery(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies: {self._stringify_dictionery(self.dev_dependencies)}"
        )
