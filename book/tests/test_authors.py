from rest_framework import status
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestAuthor:

    def test_that_anonymous_user_cant_create_author(self):
        # arrange
        client = APIClient()
        response = client.post('/authors/', {'first_name': 'ade',
                                             'last_name': 'wunmi',
                                             'email': 'ola@gamil.com'})

        # assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
