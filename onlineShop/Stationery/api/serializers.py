from rest_framework.serializers import ModelSerializer
from Stationery.models import Stationery


class StationerySerializer(ModelSerializer):
    class Meta:
        model = Stationery
        fields = '__all__'
