from rest_framework.permissions import BasePermission


class IsQuizAuthor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        author_id = getattr(obj, "author_id", None)
        if author_id is None:
            author = getattr(obj, "author", None)
            if author is None:
                return False
            author_id = author.pk
        return author_id == user.pk
