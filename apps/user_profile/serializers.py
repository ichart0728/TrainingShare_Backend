from rest_framework import serializers
from apps.user_profile.models import Profile
from apps.user.models import User

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    userProfile = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )

    class Meta:
        model = Profile
        fields = ('id', 'userProfile', 'nickName', 'gender', 'height', 'dateOfBirth')