from django.urls import path
from . import views


# defining view logic for url route and assign html tags
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),

]
