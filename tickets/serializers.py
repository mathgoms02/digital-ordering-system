from rest_framework import serializers
from .models import Ticket, TicketItem

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class TicketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketItem
        fields = "__all__"


    # Função precida ter o nome da FK para chamar dado da outra tabela
    def validate_ticket(self, value):
        if value.status == "C":
            raise serializers.ValidationError("Comanda já fechada!")
        return value