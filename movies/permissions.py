from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = "you are not an authorized user"
    def has_object_permission(self, request, view, obj):
        
        if request.method == 'GET':
            return True
        
        # if request.user == obj.owner:
        #     return True
        # else:
        #     return False
        
        ####### or #######
        
        return request.user == obj.owner
    
class IsAnAdminOrStaffUser(permissions.BasePermission):
    message = "Only admin users are allowed to edit."
    
    def has_permission(self, request, view):
        return request.user.is_staff