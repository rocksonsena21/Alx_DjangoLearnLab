from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # Anyone can read
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only owner can edit
        return obj.author == request.user