import logging
from django.shortcuts import render
from django.http import JsonResponse
import requests

# ロガーの設定
logger = logging.getLogger(__name__)

# キャッスル名のリスト（CastleIdに対応）
CASTLE_NAMES = [
    "ブラッセル", "ウィスケルケー", "モダーヴ", "シメイ", "グラベンスティン",
    "カンブル", "クインティヌス", "ランベール", "サンジャック",
    "ミヒャエル", "ナミュール", "シャルルロア", "アルゼット", "エノー",
    "ワーヴル", "モンス", "クリストフ", "コルトレイク", "イーペル",
    "サルヴァトール", "バーフ"
]

def guild_status(request):
    """APIからギルド戦情報を取得し、HTMLに変換"""
    api_url = "https://api.mentemori.icu/1017/localgvg/latest"  # APIエンドポイントを修正

    try:
        response = requests.get(api_url)
        logger.debug(f"APIレスポンス: {response.status_code}, {response.text}")
        response.raise_for_status()  # HTTPエラーなら例外発生

        data = response.json()

        # ギルド情報
        guilds = data.get("data", {}).get("guilds", {})
        castles = data.get("data", {}).get("castles", [])

        # CastleIdをキャッスル名に変換
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
                "ko_count": castle.get("LastWinPartyKnockOutCount", 0)  # KO数を追加
            })

        # HTMLテンプレートをレンダリング
        return render(request, "guild_status.html", {"castles": formatted_castles})

    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTPエラーが発生しました: {http_err}, レスポンス: {response.status_code} {response.text}")
        return JsonResponse({"error": "HTTPエラーが発生しました"}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"リクエストエラーが発生しました: {req_err}")
        return JsonResponse({"error": "リクエストエラーが発生しました"}, status=500)
    except Exception as err:
        logger.error(f"予期しないエラーが発生しました: {err}")
        return JsonResponse({"error": "予期しないエラーが発生しました"}, status=500)
