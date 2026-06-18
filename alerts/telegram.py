import os
import urllib.parse
import urllib.request

def send_telegram_message(html: str) -> bool:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "")
    if not token or not chat_id:
        print("[telegram] TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID missing. Skipping send.")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": html,
        "parse_mode": "HTML",
        "disable_web_page_preview": "true",
    }).encode()

    try:
        with urllib.request.urlopen(url, data=payload, timeout=10) as response:
            return response.status == 200
    except Exception as exc:
        print(f"[telegram] send failed: {exc}")
        return False
