from django.urls import path
from .views import guild_status,guild_form  # `fetch_guild_war_status` を削除

urlpatterns = [
    path('form/', guild_form, name='guild_form'),
    path("status/", guild_status, name="guild_status"),  # `guild_status` に変更
]
