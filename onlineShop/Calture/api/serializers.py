from rest_framework.serializers import ModelSerializer
from Calture.models import Effect


class CaltureSerializer(ModelSerializer):
    class Meta:
        model = Effect
        fields = '__all__'
