import json
import os
from crawler import get_latest_notice
from email_sender import send_email

TO_EMAIL = "xhfldkfma@naver.com"
FROM_EMAIL = "casspam0@gmail.com"
APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")  # 시크릿에서 불러옴
SEEN_FILE = "seen.json"

def load_last_seen():
    if not os.path.exists(SEEN_FILE):
        return ""
    with open(SEEN_FILE, 'r') as f:
        return json.load(f).get("last_title", "")

def save_last_seen(title):
    with open(SEEN_FILE, 'w') as f:
        json.dump({"last_title": title}, f)

def main():
    latest = get_latest_notice()
    if not latest:
        print("공지사항 없음.")
        return

    last_seen = load_last_seen()
    if latest["title"] != last_seen:
        send_email(
            subject=f"📢 새 공지: {latest['title']}",
            body=f"가톨릭대 새 공지가 올라왔어요!\n\n{latest['title']}\n{latest['link']}",
            to_email=TO_EMAIL,
            from_email=FROM_EMAIL,
            app_password=APP_PASSWORD
        )
        save_last_seen(latest["title"])
    else:
        print("🔁 새로운 공지 없음.")

if __name__ == "__main__":
    main()
  
