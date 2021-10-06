from rest_framework import serializers

from main.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "name", "surname", "uuid", "plate_number", "group", "date",
                  "direction", "status", "type_passage", "photo", "sync"]
