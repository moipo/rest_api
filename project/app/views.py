from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

#api1
class IngredientAPIView(APIView):
    def get(self, request):
        # ingredient_sr = IngredientSerializer(Ingredient.objects.all().order_by("?").first())
        ingredient_item_sr = IngredientItemSerializer(IngredientItem.objects.all().order_by("?").first())

        return Response({"data":ingredient_item_sr.data})














class Main:
    def main(request):
        ctx = {}
        return render(request,'main.html',ctx)
