"""" Users Serializers """

from rest_framework import serializers

from dezumi.users.models.User import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
