from django.urls import path
from . import views

app_name='dobox'
urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dash, name='dashboard'),
    path('ajax/add_transaction/', views.add_transaction, name='add_transaction'),
    path('ajax/create_budget/', views.create_budget, name='create_budget')
]