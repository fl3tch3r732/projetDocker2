from api.models import Personne, Group

from rest_framework import serializers

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = ['id', 'name', 'email', 'phone', 'date_created', 'date_updated']
        read_only_fields = ['date_created', 'date_updated']


class GroupeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'members', 'date_created', 'date_updated']
        read_only_fields = ['date_created', 'date_updated']
 