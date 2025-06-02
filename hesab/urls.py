from django.urls import path
from . import views



urlpatterns = [
    path('add_hesabketab/',views.add_hesabketab,name="add hesabketab"),
    path('',views.hesabketab_list,name='hesabketab_list')
]
