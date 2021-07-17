from rest_framework import permissions, viewsets

from .models import Vessel
from .serializers import VesselSerializer


class VesselViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows vessels to be viewed or edited.
    """
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
