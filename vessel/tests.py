import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory

from vessel import serializers

from .models import Vessel
from .serializers import VesselSerializer
from .views import VesselViewSet


class GetAllVesselsTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        self.factory = APIRequestFactory()
        # Create some vessels
        self.vesselA = Vessel.objects.create(
            name='Vessel A', company_id='C1', NACCS_code='N1')
        self.vesselB = Vessel.objects.create(
            name='Vessel B', company_id='C2', NACCS_code='N2')
        self.vesselC = Vessel.objects.create(
            name='Vessel C', company_id='C3', NACCS_code='N3')

    def test_vessel_create(self):
        """
        Ensure we can create a new vessel.
        """
        url = reverse('vessels-list')
        data = {'name': 'Vessel D', 'company_id': 'C4', 'NACCS_code': 'N4'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        vessel = Vessel.objects.get(NACCS_code='N4')
        serializer = VesselSerializer(vessel)
        self.assertEqual(response.data, serializer.data)

    def test_vessel_list(self):
        """
        Ensure we can retrieve all vessels.
        """
        url = reverse('vessels-list')
        response = self.client.get(url)
        all_vessels = Vessel.objects.all()
        serializer = VesselSerializer(all_vessels, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vessel_get(self):
        """
        Ensure we can retrieve a single vessel.
        """
        url = reverse('vessels-detail', kwargs={'pk': self.vesselA.pk})
        response = self.client.get(url)
        vessel = Vessel.objects.get(pk=self.vesselA.pk)
        serializer = VesselSerializer(vessel)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vessel_duplicate_NACCS_code(self):
        """
        Ensure that duplicate NACCS codes can not be created.
        """
        url = reverse('vessels-list')
        data = {'name': 'Vessel D', 'company_id': 'C4', 'NACCS_code': 'N1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
