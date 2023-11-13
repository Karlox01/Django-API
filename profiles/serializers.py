from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        # fields = '__all__' this would work if you want to specify all of the fields
        fields = [
            'id', 'owner', 'created_at', 'name',
            'content', 'image'
        ]