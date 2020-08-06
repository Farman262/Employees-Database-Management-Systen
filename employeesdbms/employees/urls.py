# from django.urls import path, include
# from employees import views

# urlpatterns = [
    
#     path('', views.home, name='home'),
#     path('home/', views.home, name='home'),
#     path('home/details/<int:id>', views.details, name='details'),   
#     path('details/<int:id>', views.details, name='details')
# ]

from django.conf.urls import url
from employees import views

urlpatterns = [
    
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/details/(?P<id>\d+)/$', views.details, name='details'),   
    url(r'^details/(?P<id>\d+)/$', views.details, name='details')
]