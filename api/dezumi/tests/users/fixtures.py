import uuid
import pytest

from rest_framework.authtoken.models import Token

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        if 'email' not in kwargs:
            kwargs['email'] = 'user@email.com'
        if 'password' not in kwargs:
            kwargs['password'] = 'strongpassword123'
        return django_user_model.objects.create_user(**kwargs)
    return make_user

@pytest.fixture
def get_or_create_token(db, create_user):
    user = create_user()
    token, _ = Token.objects.get_or_create(user=user)
    return token