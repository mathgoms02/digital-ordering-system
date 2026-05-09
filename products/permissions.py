from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        # Verifica se o usuário esta autenticado
        if not request.user or not request.user.is_authenticated:
            return False

        # Caso o método de chamada ser SAFE (nada que altere) já retorna OK
        if request.method in SAFE_METHODS:
            return True

        return request.user.groups.filter(name="admin").exists()
