from rest_framework import permissions
from django.conf import settings

class WorkshopPublicOrAdminPermission(permissions.BasePermission):
    """
    - Allows POST requests if X-API-KEY matches WORKSHOP_PUBLIC_KEY
    - Allows GET requests only for admin users
    """

    def has_permission(self, request, view):
        if request.method == "POST":
            api_key = request.headers.get("X-API-KEY")
            return api_key == settings.WORKSHOP_PUBLIC_KEY

        elif request.method == "GET":
            return request.user and request.user.is_staff  # only admin

        return False
