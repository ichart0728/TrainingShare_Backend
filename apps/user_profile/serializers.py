from rest_framework import serializers
from apps.user_profile.models import Profile, WeightHistory, BodyFatPercentageHistory, MuscleMassHistory
from apps.user.models import User

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    userProfile = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )

    class Meta:
        model = Profile
        fields = ('id', 'userProfile', 'nickName', 'gender', 'height', 'dateOfBirth')


class WeightHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightHistory
        fields = ('weight', 'date')


class BodyFatPercentageHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyFatPercentageHistory
        fields = ('bodyFatPercentage', 'date')


class MuscleMassHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleMassHistory
        fields = ('muscleMass', 'date')
