from rest_framework import permissions

class IsColecionador(permissions.BasePermission):
    """
    Permissão personalizada que permite apenas ao colecionador modificar sua coleção.
    """

    def has_object_permission(self, request, view, obj):
        # Todos os usuários podem ler (GET, HEAD ou OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Apenas o colecionador pode editar ou excluir
        return obj.colecionador == request.user
