# exchange.py
import os
from datetime import datetime
from utils import read_file, write_file

def create_exchange(chat_id, from_w, to_w, amount, valyuta, foiz, admin_id):
    ex_id = int(read_file("obmen/obmen.txt") or 0) + 1
    write_file("obmen/obmen.txt", str(ex_id))
    os.makedirs(f"obmen/{ex_id}", exist_ok=True)

    komissiya = amount * foiz / 100
    jami = amount - komissiya

    write_file(f"obmen/{ex_id}/id.txt", str(ex_id))
    write_file(f"obmen/{ex_id}/egasi.txt", str(chat_id))
    write_file(f"obmen/{ex_id}/holat.txt", "♻️ Bajarilmoqda")
    write_file(f"obmen/{ex_id}/miqdor.txt", str(jami))
    write_file(f"obmen/{ex_id}/sana.txt", datetime.now().strftime("%d.%m.%Y"))
    write_file(f"obmen/{ex_id}/vaqt.txt", datetime.now().strftime("%H:%M"))
    write_file(f"obmen/{ex_id}/valyuta.txt", f"{from_w} > {to_w}")
    write_file(f"obmen/{chat_id}/miqdor.txt", str(amount))
    write_file(f"obmen/{chat_id}/fozimiqdor.txt", str(jami))
    write_file(f"obmen/{chat_id}/obid.txt", str(ex_id))

    return ex_id, jami, komissiya

def get_exchange_info(ex_id, valyuta):
    path = f"obmen/{ex_id}"
    if not os.path.exists(path):
        return None
    info = {
        "ID": read_file(f"{path}/id.txt"),
        "Egasi": read_file(f"{path}/egasi.txt"),
        "Holat": read_file(f"{path}/holat.txt"),
        "Valyuta": read_file(f"{path}/valyuta.txt"),
        "Sana": read_file(f"{path}/sana.txt"),
        "Miqdor": f"{read_file(f'{path}/miqdor.txt')} {valyuta}"
    }
    return info

def update_exchange_status(ex_id, status):
    path = f"obmen/{ex_id}/holat.txt"
    write_file(path, status)

def save_user_exchange(chat_id, ex_id, amount, jami):
    write_file(f"obmen/{chat_id}/miqdor.txt", str(amount))
    write_file(f"obmen/{chat_id}/fozimiqdor.txt", str(jami))
    write_file(f"obmen/{chat_id}/obid.txt", str(ex_id))
