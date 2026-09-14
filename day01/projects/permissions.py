from rest_framework import permissions


class IsProjectOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        # Only logged-in users can access the endpoint
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Project owner can do anything
        if request.user == obj.user:
            return True

        # Assigned users can only view the project
        if request.user in obj.assigned_to.all():
            return request.method in permissions.SAFE_METHODS

        # Everyone else is denied
        return False
