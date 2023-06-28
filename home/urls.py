# djangotemplates/example/urls.py

from django.urls import path
from home import views

urlpatterns = [
    path(r'', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
]