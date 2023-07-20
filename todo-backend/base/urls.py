from django.urls import path
from .views import (home, create_list_view, delete_view, update_view)

urlpatterns = [
    path("", home, name="home"),
    path('api/', create_list_view),
    path('api/update/<slug:slug>/', update_view),
    path('api/delete/<slug:slug>/', delete_view),
]
