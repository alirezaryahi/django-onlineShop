from rest_framework.serializers import ModelSerializer
from Library.models import Book


class LibrarySerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
