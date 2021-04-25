from rest_framework.permissions import BasePermission, SAFE_METHODS

# a custom permission class to give access to just the owner
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user