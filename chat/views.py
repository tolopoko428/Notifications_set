from rest_framework import viewsets
from models import Notification
from serializers import NotificationsSerializer


class NotificatioViewnSet(viewsets.ModelViewSet):
    qweryset = Notification.objects.all()
    serializer_class = NotificationsSerializer
