"""" Users Serializers """

from rest_framework import serializers

from dezumi.achievements.models.Achievement import Achievement


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'
