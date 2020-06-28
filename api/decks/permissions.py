from rest_framework import permissions


class IsDeckOwnerOrContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, deck):
        if deck.owner.id == request.user.id:
            return True
        if request.user.id in tuple(map(lambda contributor: contributor.id, deck.contributors.all())):
            return True
        return False
