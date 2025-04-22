from api.models import Personne, Group

from rest_framework import serializers
from rest_framework.generics import get_object_or_404

class PersonneSerializer(serializers.ModelSerializer):

    group_display = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Personne
        fields = ['id', 'name', 'email', 'phone', 'date_created', 'date_updated', "groups", 'group_display']
        read_only_fields = ['date_created', 'date_updated']

        extra_kwargs = {
            "groups": {"write_only": True}
        }

    def get_group_display(self, obj):
        return [group.name for group in obj.groups.all()]


class GroupeSerializer(serializers.ModelSerializer):

    members = PersonneSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'members', 'date_created', 'date_updated']
        read_only_fields = ['date_created', 'date_updated']


        
 