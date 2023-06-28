from django.urls import path
from hook import views

urlpatterns = [
    path('msg/inbound/', views.inbound),
   # path('verify/', views.verify_token),
]