from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly

# Create your views here.




#api1
class IngredientItemAPIView(APIView):
    def get(self, request):
        # ingredient_sr = IngredientSerializer(Ingredient.objects.all().order_by("?").first())
        ingredient_item_sr = IngredientItemSerializer(IngredientItem.objects.all().order_by("?").first())

        return Response({"data":ingredient_item_sr.data})



#api2 - generic class
class IngredientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    # permission_classes  = (permissions.IsAuthenticatedOrReadOnly, )
    permission_classes  = (IsAdminOrReadOnly,)



#api3 - custom generic class
class CustomIngredientItemListCreateAPIView( GenericAPIView,
                                      mixins.ListModelMixin,
                                      mixins.CreateModelMixin
                                    ):
        queryset = IngredientItem.objects.all()
        serializer_class = IngredientItemSerializer
# #api 3
# class




# class IngredientItemViewset(viewsets.ModelViewSet):
#     queryset = IngredientItem.objects.all()
#     serializer_class = IngredientItemSerializer

# ==

class IngredientItemViewset(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = IngredientItem.objects.all()
    serializer_class = IngredientItemSerializer


class Main:
    def main(request):
        ctx = {}
        return render(request,'main.html',ctx)
