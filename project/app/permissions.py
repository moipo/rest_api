from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            #safe methods = get, head, options (т.е. запросы только на чтение)
            return True #return True == предоставили разрешение
        return bool(request.user and request.user.is_staff)
        #иначе даем доступ только для администратора.
