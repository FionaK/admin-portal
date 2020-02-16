from rest_framework import permissions
""" 
custom permissions to restrict what a user can perform
"""

class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # #which include GET, HEAD or OPTIONS.
        
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # Write permissions are only allowed to the owner of an object.
        return obj.owner == request.user