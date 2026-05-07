from rest_framework import viewsets
from .models import Ticket, TicketItem
from .serializers import TicketSerializer, TicketItemSerializer

# Create your views here.
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketItemViewSet(viewsets.ModelViewSet):
    queryset = TicketItem.objects.all()
    serializer_class = TicketItemSerializer
