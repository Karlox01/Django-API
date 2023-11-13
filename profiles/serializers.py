from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        # fields = '__all__' this would work if you want to specify all of the fields
        fields = [
            'id', 'owner', 'created_at', 'name',
            'content', 'image', 'is_owner'
        ]