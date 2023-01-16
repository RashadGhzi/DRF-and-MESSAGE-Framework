from rest_framework.permissions import BasePermission

class CusPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method == 'PUT':
            return True
        return False