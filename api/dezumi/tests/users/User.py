""" Testing for User """
import pytest
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from dezumi.users.models.User import User
from dezumi.tests.users.fixtures import api_client, create_user

@pytest.mark.django_db
def test_create_user(api_client):
    url = reverse('rest_register')
    data = {
        'username': 'olivertree',
        'email': 'olivertree@email.com',
        'password1': 'ridingaround',
        'password2': 'ridingaround',
        'gender': 'M',
        'birth_date': '2000-10-01'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1
    assert User.objects.get().username == 'olivertree'
    assert User.objects.get().email == 'olivertree@email.com'
    # name (Profile name) is automatically set equal to the username when the account is created.
    assert User.objects.get().name == 'olivertree'

@pytest.mark.django_db
def test_login_by_username(api_client, create_user):
    url = reverse('rest_login')
    username = 'olivertree'
    password = 'ridingaround'
    user = create_user(username=username, password=password)
    data = {
        'username': username,
        'password': password,
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert 'key' in json.loads(response.content)

@pytest.mark.django_db
def test_login_by_email(api_client, create_user):
    url = reverse('rest_login')
    password = 'ridingaround'
    user = create_user(password=password)
    data = {
        'username': user.email,
        'password': password,
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert 'key' in json.loads(response.content)
