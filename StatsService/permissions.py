from rest_framework.permissions import BasePermission, SAFE_METHODS
from ApiRequesters.Auth.permissions import IsSuperuser, IsAppTokenCorrect


class WriteFromAppReadFromSuperuserPermission(BasePermission):
    """
    Пермишн на запись с приложений и чтение суперюзером
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return IsSuperuser().has_permission(request, view)
        ans = IsAppTokenCorrect().has_permission(request, view)
        return ans
