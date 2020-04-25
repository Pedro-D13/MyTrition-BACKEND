
from django.urls import path
from foodsearch.views import ResultListView

urlpatterns = [
    # path('<str:query_string>/result/', views.result, name='result'),
    path('<str:query_string>/result/', ResultListView.as_view(), name='result'),
]
