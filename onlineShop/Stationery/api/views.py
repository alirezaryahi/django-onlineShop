from rest_framework.views import APIView
from rest_framework import generics, status
from .serializers import StationerySerializer
from Stationery.models import Stationery
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response


class AllStationery(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Stationery.objects.all()
    serializer_class = StationerySerializer


class UpdateStationery(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        query = Stationery.objects.get(pk=pk)
        serializers = StationerySerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    queryset = Stationery.objects.all()
    serializer_class = StationerySerializer
    lookup_field = 'pk'


class DeleteStationery(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        query = Stationery.objects.get(pk=pk)
        serializers = StationerySerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    queryset = Stationery.objects.all()
    serializer_class = StationerySerializer
    lookup_field = 'pk'


class PostStationery(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Stationery.objects.all()
    serializer_class = StationerySerializer
