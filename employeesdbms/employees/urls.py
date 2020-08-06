from django.urls import path, include
from employees import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('details/<int:id>', views.details, name='details')
]