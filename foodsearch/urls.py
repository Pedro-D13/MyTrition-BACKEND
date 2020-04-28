
from django.urls import path
from django.conf.urls import url, include
from foodsearch.views import ListCategoryVS,FoodDescriptionVS

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'categories', ListCategoryVS, basename='category')
router.register(r'description', FoodDescriptionVS, basename='description')

urlpatterns = [
    path('categories/<int:cat_id>/desc/<str:desc>/', FoodDescriptionVS.as_view({'get':'list'})),
    path('categories/<int:cat_id>/desc/<str:desc>/<int:fdc_id_arg>/', FoodDescriptionVS.as_view({'get':'retrieve'})),
]


urlpatterns += router.urls
    

    # path('home/',CategoryListView.as_view(), name='category-list'),
    # path('<str:query_string>/result/', ResultListView.as_view(), name='result'),

