from django.utils.translation import get_language_from_request
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from pushnotifications.api.permissions import IsOwner
from pushnotifications.api.serializers import (DeviceSerializer,
                                               CategorySerializer)
from pushnotifications.models import Device, Category


class DeviceViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get_queryset(self):
        # filter all devices to only those belonging to the current user
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        language = get_language_from_request(self.request)

        try:
            serializer.instance = Device.objects.get(
                user=self.request.user,
                registration_id=serializer.validated_data['registration_id']
            )
        except Device.DoesNotExist:
            pass
        data = serializer.validated_data
        if 'receive_category' in data and len(data['receive_category']) > 0:
            categories = data['receive_category'] + ['general']
            serializer.save(user=self.request.user, language=language,
                            receive_category=categories)
        else:
            categories = [c.pk for c in Category.objects.all()]
            serializer.save(user=self.request.user, language=language,
                            receive_category=categories)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False)
    def categories(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
