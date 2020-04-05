from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="HOME"),
    path('sum', views.add),
    path('to_calc', views.calc),
]