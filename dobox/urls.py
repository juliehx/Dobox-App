from django.urls import path
from . import views

app_name='dobox'
urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('success/', views.success, name='success')
]