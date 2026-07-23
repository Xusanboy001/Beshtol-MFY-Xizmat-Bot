import telebot
from telebot import types
import psycopg2
import os
import time

# ==================================
# BESHTOL MFY XIZMAT BOTI v2.0
# Muallif: Mirzaqosimov Xusanboy
# ==================================

TOKEN = "8872934581:AAGObQZlY357TfzAgnSATK7e5-GBgvWgx2s"

# ==========================
# ADMIN
# ==========================

ADMIN_ID = 8786347772

# ==========================
# XODIMLAR ID
# ==========================

RAIS_ID = 111111111
HOKIM_ID = 8922059700
YOSHLAR_ID = 333333333
IJTIMOIY_ID = 444444444
XOTIN_QIZLAR_ID = 555555555
PROFILAKTIKA_ID = 666666666
SOLIQ_ID =777777777 
ELEKTR_ID = 888888881
SUV_ID = 888888882
GAZ_ID = 888888883

# ==========================
# BOT
# ==========================

bot = telebot.TeleBot(TOKEN)

# ==========================
# AI TAHLIL
# ==========================
def ai_department(text):
    t = text.lower()
    if any(x in t for x in ["svet","elektr","tok","chiroq"]):
        return "⚡ Elektr hodimi","Yuqori"
    elif "gaz" in t:
        return "🔥 Gaz hodimi","Yuqori"
    elif "suv" in t:
        return "💧 Suv hodimi","O'rta"
    elif any(x in t for x in [
        "yosh",
        "student",
        "kontrakt",
        "kontrakt to'lash",
        "yoshlar daftari",
        "daftar",
        "stipendiya",
        "grant",
        "o'qish",
        "universitet",
        "institut",
        "talaba",
        "ishsiz yosh",
        "bandlik",
        "kasb",
        "o'quv kursi"
    ]):
        return "🧑‍🎓 Yoshlar yetakchisi","O'rta"
    elif any(x in t for x in [
        "nafaqa","yordam","moddiy","ijtimoiy yordam","bolalar puli","bola puli","nafaqa puli"
    ]):
        return "👨 Ijtimoiy xodim","O'rta"
    elif any(x in t for x in [
        "ayol","xotin","qiz","ayollar daftari","ayollar"
    ]):
        return "👩 Xotin-qizlar faoli","O'rta"
    elif any(x in t for x in ["o'g'ri","urish","bezor"]):
        return "👮 Profilaktika inspektori","Yuqori"
    
    elif any(x in t for x in [
        "kredit",
        "imtiyozli kredit",
        "biznes",
        "tadbirkorlik",
        "tadbirkor",
        "o'zini o'zi band",
        "o'zini o'zi band qilish",
        "subsidiya",
        "biznes reja",
        "loyiha",
        "ish boshlash",
        "issiqxona",
        "chorvachilik",
        "parrandachilik",
        "hunarmandchilik"
    ]):
        return "💼 Hokim yordamchisi","O'rta"

return "👤 Mahalla raisi","O'rta"


state = {}
admin_state = {}
reply_messages = {}

# ==========================
# DATABASE
# ==========================

DATABASE_URL = os.environ.get("DATABASE_URL")

db = psycopg2.connect(DATABASE_URL)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id BIGINT PRIMARY KEY,
    fullname TEXT
)
""")

db.commit()

# ==========================
# FOYDALANUVCHI QO'SHISH
# ==========================

def add_user(message):

    cursor.execute(
        "SELECT user_id FROM users WHERE user_id = %s",
        (message.chat.id,)
    )

    user = cursor.fetchone()

    if user is None:

        cursor.execute(
            "INSERT INTO users (user_id, fullname) VALUES (%s, %s)",
            (
                message.chat.id,
                message.from_user.first_name
            )
        )

        db.commit()

# ==========================
# STATISTIKA
# ==========================

def users_count():

    cursor.execute("SELECT COUNT(*) FROM users")

    return cursor.fetchone()[0]

# ==========================
# ASOSIY MENYU
# ==========================

def menu():

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row("👤 Mahalla raisi","💼 Hokim yordamchisi")
    kb.row("👨 Ijtimoiy xodim","🧑‍🎓 Yoshlar yetakchisi")
    kb.row("👩 Xotin-qizlar faoli","👮 Profilaktika inspektori")
    kb.row("💰 Soliq inspektori","📍 Mahalla manzili")
    kb.row("☎️ Tezkor xizmatlar","📢 Mahalla e'lonlari")
    kb.row("📝 Murojaat yuborish")

    return kb

# ==========================
# START
# ==========================

@bot.message_handler(commands=["start"])
def start(message):

    add_user(message)

    text = f"""
🏠 Assalomu alaykum!

👨‍💻 Muallif: Mirzaqosimov Xusanboy
📞 Shikoyat va takliflar:
+998 97 987 42 43

━━━━━━━━━━━━━━━━━━━━━━

Beshtol MFY Xizmat Botiga xush kelibsiz! 😊

Siz ushbu bot orqali:

✅ Mahalla xodimlari
✅ Mahalla e'lonlari
✅ Murojaatlar
✅ Tezkor xizmatlar
✅ Mahalla manzili

bo'yicha ma'lumot olishingiz mumkin.

👇 Kerakli bo'limni tanlang.
"""

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=menu()
    )
    
    
    # ==========================
# 👤 MAHALLA RAISI
# ==========================

@bot.message_handler(func=lambda m: m.text == "👤 Mahalla raisi")
def rais(message):
    bot.send_message(
        message.chat.id,
        f"""
👤 Mahalla raisi

📛 F.I.Sh:
Mamadaliyeva Nafisaxon


🏢 Ish joyi:
Beshtol MFY binosi

📞 Telefon:
+998 88 431 79 79

🕘 Qabul vaqti:
Dushanba - Juma
09:00 - 18:00

🏢 Manzil:
Beshtol MFY binosi
"""
    )


# ==========================
# 💼 HOKIM YORDAMCHISI
# ==========================

@bot.message_handler(func=lambda m: m.text == "💼 Hokim yordamchisi")
def hokim(message):
    bot.send_message(
        message.chat.id,
        f"""
💼 Hokim yordamchisi

📛 F.I.Sh:
Temirov Dostonbek


🏢 Ish joyi:
Beshtol MFY binosi

📞 Telefon:
+998 97 472 76 76

🕘 Qabul vaqti:
Dushanba - Juma
09:00 - 18:00
"""
    )


# ==========================
# 👨 IJTIMOIY XODIM
# ==========================

@bot.message_handler(func=lambda m: m.text == "👨 Ijtimoiy xodim")
def ijtimoiy(message):
    bot.send_message(
        message.chat.id,
        f"""
👨 Ijtimoiy xodim

📛 F.I.Sh:
G'ulomov Azizullo

🏢 Ish joyi:
Beshtol MFY binosi

📞 Telefon:
+998880086842

🕘 Qabul vaqti:
09:00 - 18:00
"""
    )


# ==========================
# 🧑‍🎓 YOSHLAR YETAKCHISI
# ==========================

@bot.message_handler(func=lambda m: m.text == "🧑‍🎓 Yoshlar yetakchisi")
def yoshlar(message):
    bot.send_message(
        message.chat.id,
        f"""
🧑‍🎓 Yoshlar yetakchisi

📛 F.I.Sh:
Toxtasinov Azizullo

🏢 Ish joyi:
Beshtol MFY binosi

📞 Telefon:
+998905289800

🕘 Qabul vaqti:
09:00 - 18:00
"""
    )


# ==========================
# 👩 XOTIN-QIZLAR FAOLI
# ==========================

@bot.message_handler(func=lambda m: m.text == "👩 Xotin-qizlar faoli")
def xotin_qizlar(message):
    bot.send_message(
        message.chat.id,
        f"""
👩 Xotin-qizlar faoli

📛 F.I.Sh:
Alixonova Umidaxon

🏢 Ish joyi:
Beshtol MFY binosi

📞 Telefon:
+998916056607

🕘 Qabul vaqti:
09:00 - 18:00
"""
    )


# ==========================
# 👮 PROFILAKTIKA INSPEKTORI
# ==========================

@bot.message_handler(func=lambda m: m.text == "👮 Profilaktika inspektori")
def profilaktika(message):
    bot.send_message(
        message.chat.id,
        f"""
👮 Profilaktika inspektori

📛 F.I.Sh:
Maxmudov Mirjalol

🏢 Ish joyi:
Beshtol MFY binosi

📞 Telefon:
+998934293135

🕘 Qabul vaqti:
09:00 - 18:00
"""
    )


# ==========================
# 💰 SOLIQ INSPEKTORI
# ==========================

@bot.message_handler(func=lambda m: m.text == "💰 Soliq inspektori")
def soliq(message):
    bot.send_message(
        message.chat.id,
        """
💰 Soliq inspektori

📛 F.I.Sh:
Ma'lumot kiritilmagan

🏢 Ish joyi:
Beshtol MFY binosi

📞 Telefon:
Ma'lumot kiritilmagan

🕘 Qabul vaqti:
09:00 - 18:00
"""
    )


# ==========================
# 📍 MAHALLA MANZILI
# ==========================

@bot.message_handler(func=lambda m: m.text == "📍 Mahalla manzili")
def manzil(message):
    bot.send_message(
        message.chat.id,
        """
📍 Beshtol MFY

📌 Andijon viloyati
Jalaquduq tumani
Beshtol MFY

🕘 Ish vaqti:
09:00 - 18:00
"""
    )


# ==========================
# ☎️ TEZKOR XIZMATLAR
# ==========================

@bot.message_handler(func=lambda m: m.text == "☎️ Tezkor xizmatlar")
def tezkor(message):
    bot.send_message(
        message.chat.id,
        """
☎️ Tezkor xizmatlar

🚒 101 — Yong'in

👮 102 — Ichki ishlar

🚑 103 — Tez yordam

💨 104 — Gaz

⚡ 1154 — Elektr

🚨 1050 — FVV
"""
    )
    
    
# ==========================
# 📢 MAHALLA E'LONLARI
# ==========================

last_elon = "📭 Hozircha e'lon mavjud emas."

@bot.message_handler(func=lambda m: m.text == "📢 Mahalla e'lonlari")
def show_elon(message):
    bot.send_message(message.chat.id, last_elon)


# ==========================
# ADMIN PANEL
# ==========================

admin_state = {}

@bot.message_handler(commands=["admin"])
def admin(message):

    if message.chat.id != ADMIN_ID:
        bot.send_message(
            message.chat.id,
            "⛔ Siz admin emassiz."
        )
        return

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row("📊 Statistika")
    kb.row("📢 E'lon yuborish")
    kb.row("🏠 Asosiy menyu")

    bot.send_message(
        message.chat.id,
        "👨‍💼 Admin panel",
        reply_markup=kb
    )


# ==========================
# STATISTIKA
# ==========================

@bot.message_handler(func=lambda m: m.text == "📊 Statistika")
def statistika(message):

    if message.chat.id != ADMIN_ID:
        return

    cursor.execute("SELECT COUNT(*) FROM users")

    soni = cursor.fetchone()[0]

    bot.send_message(
        message.chat.id,
        f"""
📊 BOT STATISTIKASI

👥 Foydalanuvchilar soni:

{soni} ta
"""
    )


# ==========================
# E'LON YUBORISH
# ==========================

@bot.message_handler(func=lambda m: m.text == "📢 E'lon yuborish")
def elon(message):

    if message.chat.id != ADMIN_ID:
        return

    admin_state[message.chat.id] = "elon"

    bot.send_message(
        message.chat.id,
        """
📢 Yubormoqchi bo'lgan
e'lon matnini yuboring.
"""
    )


# ==========================
# ASOSIY MENYU
# ==========================

@bot.message_handler(func=lambda m: m.text == "🏠 Asosiy menyu")
def asosiy(message):

    bot.send_message(
        message.chat.id,
        "🏡 Asosiy menyu",
        reply_markup=menu()
    )
    
    
# ==========================
# MUROJAAT YUBORISH
# ==========================

@bot.message_handler(func=lambda m: m.text == "📝 Murojaat yuborish")
def request(message):

    state[message.chat.id] = "request"

    bot.send_message(
        message.chat.id,
        "✍️ Murojaatingizni yozing."
    )


@bot.message_handler(func=lambda m: state.get(m.chat.id) == "request")
def request_text(message):

    state.pop(message.chat.id)

    bot.send_message(message.chat.id,"🤖 Sun'iy intellekt murojaatingizni tahlil qilmoqda...")
    time.sleep(2)
    department, level = ai_department(message.text)
    bot.send_message(message.chat.id,
        f"✅ Tahlil yakunlandi.\n\n📌 Mas'ul: {department}\n🔥 Muhimlik: {level}")

    text = f"""
📩 YANGI MUROJAAT

🤖 AI:
Mas'ul: {department}
Muhimlik: {level}

📩 YANGI MUROJAAT

👤 {message.from_user.first_name}

🆔 {message.chat.id}

✍️

{message.text}
"""

    bot.send_message(ADMIN_ID, text)

    # AI aniqlagan murojaatni mas'ullarga yuborish
    if department == "⚡ Elektr hodimi":
        bot.send_message(ELEKTR_ID, text)
        bot.send_message(RAIS_ID, text)

    elif department == "💧 Suv hodimi":
        bot.send_message(SUV_ID, text)
        bot.send_message(RAIS_ID, text)

    elif department == "🔥 Gaz hodimi":
        bot.send_message(GAZ_ID, text)
        bot.send_message(RAIS_ID, text)

    bot.send_message(
        message.chat.id,
        """✅ Murojaatingiz yuborildi.

Tez orada javob beriladi.""",
        reply_markup=menu()
    )
    
    
# ==========================
# E'LONNI BARCHAGA YUBORISH
# ==========================

@bot.message_handler(func=lambda m: admin_state.get(m.chat.id) == "elon")
def send_elon(message):

    global last_elon

    admin_state.pop(message.chat.id)

    last_elon = f"""
📢 MAHALLA E'LONI

{message.text}
"""

    cursor.execute(
        "SELECT user_id FROM users"
    )

    users = cursor.fetchall()

    soni = 0

    for user in users:

        try:

            bot.send_message(
                user[0],
                last_elon
            )

            soni += 1

        except Exception as e:

            print(e)

    bot.send_message(
        message.chat.id,
        f"""
✅ E'lon yuborildi.

👥 {soni} ta foydalanuvchiga yuborildi.
"""
    )


# ==========================
# BOTNI ISHGA TUSHIRISH
# ==========================

print("Bot ishga tushdi...")

bot.infinity_polling(skip_pending=True)
     