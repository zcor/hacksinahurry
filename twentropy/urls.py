from django.urls import path
from . import views

urlpatterns = [
            path('', views.index, name='index'),
            path('scrape', views.scrape, name='scrape'),
            path('insights', views.insights, name='insights'),
            ]

