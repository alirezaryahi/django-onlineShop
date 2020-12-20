from rest_framework.views import APIView
from rest_framework import generics, status
from .serializers import LibrarySerializer
from Library.models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response


class AllBooks(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = LibrarySerializer


class UpdateBooks(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializers = LibrarySerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    queryset = Book.objects.all()
    serializer_class = LibrarySerializer
    lookup_field = 'pk'


class DeleteBooks(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializers = LibrarySerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    queryset = Book.objects.all()
    serializer_class = LibrarySerializer
    lookup_field = 'pk'


class PostBooks(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = LibrarySerializer
