from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import generics, status
from .serializers import LibrarySerializer
from Library.models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.response import Response


class AllBooks(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = LibrarySerializer
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            queryset = Book.objects.filter(
                Q(category__title__icontains=query) |
                Q(title__icontains=query) |
                Q(description__icontains=query+' ')
            )
            return queryset
        else:
            return Book.objects.all()    


class UpdateBooks(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = LibrarySerializer
    lookup_field = 'pk'


class DeleteBooks(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = LibrarySerializer
    lookup_field = 'pk'


class PostBooks(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = LibrarySerializer
