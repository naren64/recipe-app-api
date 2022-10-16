"""
views for recipe api's
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    """view for manage recipe api's """
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication = TokenAuthentication
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ retrieve recipes for authenticated users"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """ return the serializer class for request"""
        return serializers.RecipeSerializer if self.action == 'list' else self.serializer_class
