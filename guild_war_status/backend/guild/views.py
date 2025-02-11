from django.shortcuts import render, redirect
import logging
import requests

logger = logging.getLogger(__name__)

CASTLE_NAMES = [
    "ブラッセル", "ウィスケルケー", "モダーヴ", "シメイ", "グラベンスティン",
    "カンブル", "クインティヌス", "ランベール", "サンジャック",
    "ミヒャエル", "ナミュール", "シャルルロア", "アルゼット", "エノー",
    "ワーヴル", "モンス", "クリストフ", "コルトレイク", "イーペル",
    "サルヴァトール", "バーフ"
]

def guild_form(request):
    """ギルド戦フォームを表示"""
    return render(request, "guild_form.html")

def guild_status(request):
    """APIからギルド戦情報を取得し、結果ページにリダイレクト"""

    if request.method == "POST":
        server = request.POST.get("server", "1")
        world = request.POST.get("world", "").strip()
    else:
        server = "1"
        world = ""

    world_id = f"{server}{world}" if world else f"{server}"
    api_url = f"https://api.mentemori.icu/{world_id}/localgvg/latest"

    try:
        response = requests.get(api_url)
        logger.debug(f"APIリクエスト: {api_url}")
        logger.debug(f"APIレスポンス: {response.status_code}, {response.text}")
        response.raise_for_status()

        data = response.json()
        guilds = data.get("data", {}).get("guilds", {})
        castles = data.get("data", {}).get("castles", [])

        formatted_castles = []
        for castle in castles:
            castle_id = castle.get("CastleId", 0)
            castle_name = CASTLE_NAMES[castle_id - 1] if 1 <= castle_id <= len(CASTLE_NAMES) else f"Unknown ({castle_id})"
            guild_id = str(castle.get("GuildId", ""))
            attacker_guild_id = str(castle.get("AttackerGuildId", ""))

            formatted_castles.append({
                "castle_name": castle_name,
                "guild_name": guilds.get(guild_id, "Unknown Guild"),
                "attacker_guild_name": guilds.get(attacker_guild_id, "No Attacker"),
                "attack_party_count": castle.get("AttackPartyCount", 0),
                "defense_party_count": castle.get("DefensePartyCount", 0),
                "state": "Occupied" if castle.get("GvgCastleState", 0) == 1 else "Free",
                "ko_count": castle.get("LastWinPartyKnockOutCount", 0)
            })

        return render(request, "guild_status.html", {
            "castles": formatted_castles,
            "server": server,
            "world": world
        })

    except Exception as err:
        logger.error(f"エラー発生: {err}")
        return render(request, "guild_status.html", {
            "castles": [],
            "server": server,
            "world": world,
            "error": "データ取得に失敗しました"
        })
