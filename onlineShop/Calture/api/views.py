from rest_framework.views import APIView
from rest_framework import generics, status
from .serializers import CaltureSerializer
from Calture.models import Effect
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response


class AllCalture(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Effect.objects.all()
    serializer_class = CaltureSerializer


class UpdateCalture(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        query = Effect.objects.get(pk=pk)
        serializers = CaltureSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    queryset = Effect.objects.all()
    serializer_class = CaltureSerializer
    lookup_field = 'pk'


class DeleteCalture(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        query = Effect.objects.get(pk=pk)
        serializers = CaltureSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    queryset = Effect.objects.all()
    serializer_class = CaltureSerializer
    lookup_field = 'pk'


class PostCalture(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Effect.objects.all()
    serializer_class = CaltureSerializer
