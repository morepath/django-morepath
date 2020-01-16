import pytest

from testapp.models import Person


def test_root(client):
    r = client.get("/")
    assert r.json() == {"hello": "world!"}


@pytest.mark.django_db
def test_person_get(client):
    person = Person.objects.create(first_name="Bob", last_name="Bobson")
    r = client.get(f"/persons/{person.id}")
    assert r.json() == {"first_name": "Bob", "last_name": "Bobson"}
