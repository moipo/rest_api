from .models import *
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class IngredientItemSerializer(serializers.ModelSerializer):
    amount_2x = serializers.SerializerMethodField()
    ingredient = IngredientSerializer( many = False)

    class Meta:
        model = IngredientItem
        fields = "__all__"

    def get_amount_2x(self, obj):
        return obj.amount * 2
