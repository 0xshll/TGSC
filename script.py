from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest, InviteToChannelRequest
from telethon.tl.types import ChannelParticipantsSearch
import time
import asyncio
import os

api_id = int(input("ادخل API ID: "))
api_hash = input("ادخل API HASH: ")

session_name = 'spider_session'
client = TelegramClient(session_name, api_id, api_hash)

async def transfer_members():
    from_group = input("رابط الجروب اللي هتسحب منه: ")
    to_group = input("رابط الجروب اللي هتضيف فيه: ")
    limit = int(input("عدد الأعضاء اللي عايز تنقلهم: "))

    from_chat = await client.get_entity(from_group)
    to_chat = await client.get_entity(to_group)

    participants = await client(GetParticipantsRequest(
        channel=from_chat,
        filter=ChannelParticipantsSearch(''),
        offset=0,
        limit=limit,
        hash=0
    ))

    users = participants.users
    print(f"\nتم العثور على {len(users)} عضو. جاري محاولة الإضافة...\n")

    added = 0
    failed_users = []

    for user in users:
        try:
            await client(InviteToChannelRequest(
                channel=to_chat,
                users=[user.id]
            ))
            print(f"✅ تمت إضافة: {user.first_name}")
            added += 1
        except Exception as e:
            error = str(e).lower()
            name = user.first_name if hasattr(user, 'first_name') else "عضو"

            if "seconds" in error:
                print("⛔ تيليجرام عمل حظر مؤقت. لازم تستنى.")
                break
            elif "privacy" in error or "can't be invited" in error:
                print(f"❌ {name} قافل إعدادات الإضافة.")
                failed_users.append(user.username or name)
            else:
                print(f"⚠️ فشل مع {name}: {e}")
                failed_users.append(user.username or name)

        time.sleep(5)

    if failed_users:
        with open("failed.txt", "w", encoding="utf-8") as f:
            for u in failed_users:
                f.write(f"{u}\n")

    print(f"\n✅ تم الانتهاء. تمت إضافة {added} عضو. المحاولات الفاشلة محفوظة في failed.txt\n")

async def main():
    while True:
        print("\n--- قائمة Spider Calls ---")
        print("1 - نقل الأعضاء من جروب لجروب")
        print("2 - خروج")
        print("3 - حذف السيشن الحالي وتسجيل برقم جديد")

        choice = input("اختر رقم العملية: ")

        if choice == "1":
            await transfer_members()
        elif choice == "2":
            print("خروج...")
            break
        elif choice == "3":
            try:
                session_files = [
                    f'{session_name}.session',
                    f'{session_name}.session-journal'
                ]
                for file in session_files:
                    if os.path.exists(file):
                        os.remove(file)
                print("✅ تم حذف الجلسة. أعد تشغيل السكربت لتسجيل الدخول برقم جديد.")
                break
            except Exception as e:
                print(f"❌ حصل خطأ أثناء حذف السيشن: {e}")
        else:
            print("❌ اختيار غير صحيح")

with client:
    client.loop.run_until_complete(main())
