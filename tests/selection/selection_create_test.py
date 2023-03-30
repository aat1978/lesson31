import pytest
from rest_framework import status

from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, user_access_token):
    user, access_token = user_access_token
    ad_list = AdFactory.create_batch(10)

    data = {
        "name": "Имя подборки",
        "items": [ad.pk for ad in ad_list]
    }
    expected_data = {
        "id": 7,
        "owner": user.username,
        "name": "Имя подборки",
        "items": [ad.pk for ad in ad_list]
    }

    response = client.post("/selection/", data=data, HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_data
