# api/permissions.py

from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Custom permission to only allow admin users to make changes.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
