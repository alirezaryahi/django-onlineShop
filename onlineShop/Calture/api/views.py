from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import generics, status
from .serializers import CaltureSerializer
from Calture.models import Effect
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.response import Response


class AllCalture(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CaltureSerializer

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            queryset = Effect.objects.filter(
                Q(subject__title__icontains=query) |
                Q(title__icontains=query) |
                Q(description__icontains=query+' ')
            )
            return queryset
        else:
            return Effect.objects.all()


class UpdateCalture(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Effect.objects.all()
    serializer_class = CaltureSerializer
    lookup_field = 'pk'


class DeleteCalture(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Effect.objects.all()
    serializer_class = CaltureSerializer
    lookup_field = 'pk'


class PostCalture(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Effect.objects.all()
    serializer_class = CaltureSerializer
