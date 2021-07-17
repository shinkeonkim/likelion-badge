from django.urls import path
from .views import likelion_shield_badge, likelion_university_badge_v1

app_name = 'api'

urlpatterns = [
    path('likelion_shield_badge', likelion_shield_badge),
    path('likelion_university_badge/v1', likelion_university_badge_v1),
]
