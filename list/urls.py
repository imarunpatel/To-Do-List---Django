from django.urls import path
from .views import home, UpdatedList

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('list', UpdatedList.as_view(), name='list')
]