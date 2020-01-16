import morepath
from .models import Person


class App(morepath.App):
    pass


@App.path(path="")
class Root(object):
    pass


@App.json(model=Root)
def hello_world(self, request):
    return {"hello": "world!"}


@App.path(model=Person, path="/persons/{id}")
def get_person(id=0):
    return Person.objects.filter(pk=id).first()


@App.json(model=Person)
def person_get(self, request):
    return {"first_name": self.first_name, "last_name": self.last_name}


app = App()
