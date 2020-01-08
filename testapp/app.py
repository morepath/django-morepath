import morepath


class App(morepath.App):
    pass


@App.path(path="")
class Root(object):
    pass


@App.json(model=Root)
def hello_world(self, request):
    return {"hello": "world!"}


app = App()
