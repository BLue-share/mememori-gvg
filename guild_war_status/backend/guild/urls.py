from django.urls import path
from .views import guild_status  # `fetch_guild_war_status` を削除

urlpatterns = [
    path("status/", guild_status, name="guild_status"),  # `guild_status` に変更
]
