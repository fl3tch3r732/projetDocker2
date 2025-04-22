
from rest_framework import viewsets

from api.models import Personne, Group
from api.manager.serializers import PersonneSerializer, GroupeSerializer
  
class PersonneViewSet(viewsets.ModelViewSet):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupeSerializer
