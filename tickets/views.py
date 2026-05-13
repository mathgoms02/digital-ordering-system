from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Ticket, TicketItem
from .serializers import TicketSerializer, TicketItemSerializer


# Create your views here.
class TicketViewSet(viewsets.ModelViewSet):
    # Pesquisar para apenas o bartender responsável conseguir ver a comanda
    # queryset = Ticket.objects.filter(bartender=requests.user)

    queryset = Ticket.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer

    def get_queryset(self):
        logged_user = self.request.user

        if logged_user.groups.filter(name="admin").exists() or logged_user.is_superuser:
            return Ticket.objects.all()
        return Ticket.objects.filter(bartender=logged_user)

    # Salvando bartender pelo Token (login)
    def perform_create(self, serializer):
        serializer.save(bartender=self.request.user)


class TicketItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = TicketItem.objects.all()
    serializer_class = TicketItemSerializer

    def perform_create(self, serializer):
        selected_product = serializer.validated_data.get("product")
        serializer.save(unit_value=selected_product.unit_value)
