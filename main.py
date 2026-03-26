import time
import traceback
from handlers import handle_message, handle_callback
from utils import bot

def main():
    print("🚀 Bot ishga tushdi!")
    offset = 0
    while True:
        try:
            resp = bot("getUpdates", {"offset": offset, "timeout": 30})
            if resp.get("ok"):
                for upd in resp.get("result", []):
                    msg = upd.get("message")
                    cb = upd.get("callback_query")
                    if msg:
                        chat = msg["chat"]["id"]
                        txt = msg.get("text", "")
                        user = msg["from"].get("username", "")
                        mid = msg["message_id"]
                        handle_message(chat, txt, user, mid)
                    elif cb:
                        chat = cb["message"]["chat"]["id"]
                        mid = cb["message"]["message_id"]
                        cid = cb["id"]
                        d = cb["data"]
                        handle_callback(cid, chat, mid, d)
                    offset = upd["update_id"] + 1
            time.sleep(1)
        except Exception as e:
            print(f"Xatolik: {e}\n{traceback.format_exc()}")
            time.sleep(5)

if __name__ == "__main__":
    main()
