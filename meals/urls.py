from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('add/',views.add_meal,name='add'),
    path('edit/<int:pk>/',views.edit_meal,name='edit'),
    path('delete/<int:pk>/',views.delete_meal,name='delete'),
]