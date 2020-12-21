from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics, status
from django.db.models import Q
from .serializers import StationerySerializer
from Stationery.models import Stationery
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.response import Response


class AllStationery(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Stationery.objects.all()
    serializer_class = StationerySerializer
    filterset_fields = ['group', 'title', 'description']
    search_fields = ['group', 'title', 'description']
    
    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     if query:
    #         queryset = Stationery.objects.filter(
    #             Q(group__title__icontains=query) |
    #             Q(title__icontains=query) |
    #             Q(description__icontains=query+' ')
    #         )
    #         return queryset
    #     else:
    #         return Stationery.objects.all()

class UpdateStationery(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Stationery.objects.all()
    serializer_class = StationerySerializer
    lookup_field = 'pk'


class DeleteStationery(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Stationery.objects.all()
    serializer_class = StationerySerializer
    lookup_field = 'pk'


class PostStationery(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Stationery.objects.all()
    serializer_class = StationerySerializer
