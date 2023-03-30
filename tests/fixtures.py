import pytest


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = "test_username"
    password = "test_password"
    django_user_model.objects.create_user(username=username, password=password, role="admin")

    response = client.post("/user/token/", {"username": username, "password": password})

    return response.data.get("access")


@pytest.fixture
@pytest.mark.django_db
def user_access_token(client, django_user_model):
    username = "test_username"
    password = "test_password"
    new_user = django_user_model.objects.create_user(username=username, password=password, role="admin")

    response = client.post("/user/token/", {"username": username, "password": password})

    return new_user, response.data.get("access")
