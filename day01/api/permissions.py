from rest_framework import permissions
class IsUserOwnerOrGetPost(permissions.BasePermission):
    def has_permission(self, request, view):
            return True # it  means everyone can access the GET, HEAD, OPTIONS requests


    def has_object_permission(self, request, view, obj):
          if request.method in permissions.SAFE_METHODS:    # GET, HEAD or OPTIONS requests
              return True


          if not request.user.is_anonymous:
              return request.user == obj # Only the owner of the object can modify it

          return False  # Deny access for anonymous users

class IsProfileUserOrGetProfile(permissions.BasePermission):
     def has_permission(self,request,view):
          return True 

     def has_object_permission(self,request,view,obj):
          if request.method in permissions.SAFE_METHODS:
               return True 

          if not request.user.is_anonymous:
               return request.user.profile == obj 

          return False 