from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying yo edit their own profile"""
        if request.method is permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
