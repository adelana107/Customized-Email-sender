from django.urls import path
from . import views



urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    path('success/', views.success, name='success'),
    path('unauthorized/', views.unauthorized_view, name='unauthorized'),

]

