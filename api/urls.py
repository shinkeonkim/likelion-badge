from django.urls import path
from .views import likelion_shield_badge

app_name = 'api'

urlpatterns = [
  path('likelion_shield_badge', likelion_shield_badge),
]
