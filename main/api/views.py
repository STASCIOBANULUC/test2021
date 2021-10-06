from rest_framework import viewsets

from main.api.serializers import TransactionSerializer
from main.models import Transaction


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
