from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketItemViewSet, TicketViewSet

router = DefaultRouter()
router.register(r'tickets', TicketViewSet)
router.register(r'ticketsItem', TicketItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]