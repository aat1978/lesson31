import pytest


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = "test"
    password = "test"
    django_user_model.objects.create(username=username, password=password, role="admin")

    response = client.post("/user/token/", {"username": username, "password": password})

    return response.data.get("access")
