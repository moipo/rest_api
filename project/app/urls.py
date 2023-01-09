from django.urls import path, include, re_path
from .views import *

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'ingredient_items', IngredientItemViewset)

urlpatterns = [
    path('', Main.main, name = 'main'),

    #подключение аутентификации и авторизации DRF
    path('built_in_session_auth/', include('rest_framework.urls')),

    path('api1/',IngredientItemAPIView.as_view()),
    path('api2/ingredients/',IngredientListCreateAPIView.as_view()),
    path('api2/ingredients/<int:id>',IngredientListCreateAPIView.as_view()),
    path('api3/ingredient_items/<int:id>/',CustomIngredientItemListCreateAPIView.as_view()),
    # path('api4/ingredient_items/',IngredientItemViewset.as_view({"get" : "list"})),
    # path('api4/ingredient_items/<int:id>',IngredientItemViewset.as_view({"put" : "update"})),
    path('api4/',include(router.urls)),
    path('api5/auth',include("djoser.urls")),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
