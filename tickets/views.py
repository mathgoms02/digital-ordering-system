from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Ticket, TicketItem
from .serializers import TicketSerializer, TicketItemSerializer


# Create your views here.
class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    # Salvando bartender pelo Token (login)
    def perform_create(self, serializer):
        serializer.save(bartender=self.request.user)


class TicketItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = TicketItem.objects.all()
    serializer_class = TicketItemSerializer
