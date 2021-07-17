from rest_framework import serializers
from .models import Vessel

class VesselSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vessel
        fields = ['id', 'name', 'company_id', 'NACCS_code']