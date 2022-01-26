"""" Users Serializers """

from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from dezumi.others.constants import GENDER
from dezumi.users.models.User import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CustomRegisterSerializer(RegisterSerializer):
    """ 
    Custom Register Serializer for dj-rest-auth.
    Add optionals fields "Birthdate", "Country" and "Gender"
    """

    birth_date = serializers.DateField(required=False)
    gender = serializers.ChoiceField(choices=GENDER, required=False)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.name = self.data.get('username')
        user.birth_date = self.data.get('birth_date')
        user.country = self.data.get('country')
        user.gender = self.data.get('gender')
        user.save()
        return user
