from django.urls import path
from .views import *

urlpatterns = [
    path('', Main.main, name = 'main'),
    path('api1',IngredientAPIView.as_view())
]
