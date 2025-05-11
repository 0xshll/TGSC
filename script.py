from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest, InviteToChannelRequest
from telethon.tl.types import ChannelParticipantsSearch
import time
import asyncio
import os

api_id = int(input("Enter your API ID: "))
api_hash = input("Enter your API HASH: ")

session_name = 'spider_session'
client = TelegramClient(session_name, api_id, api_hash)

async def transfer_members():
    from_group = input("Enter the source group username or link: ")
    to_group = input("Enter the target group username or link: ")
    limit = int(input("How many members to transfer: "))

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
    print(f"\nFound {len(users)} users. Starting transfer...\n")

    added = 0
    failed_users = []

    for user in users:
        try:
            await client(InviteToChannelRequest(
                channel=to_chat,
                users=[user.id]
            ))
            print(f"✅ Added: {user.first_name}")
            added += 1
        except Exception as e:
            error = str(e).lower()
            name = user.first_name if hasattr(user, 'first_name') else "User"

            if "seconds" in error:
                print("⛔ Telegram rate limit reached. Try again later.")
                break
            elif "privacy" in error or "can't be invited" in error:
                print(f"❌ {name} has invite restrictions.")
                failed_users.append(user.username or name)
            else:
                print(f"⚠️ Failed to add {name}: {e}")
                failed_users.append(user.username or name)

        time.sleep(5)

    if failed_users:
        with open("failed.txt", "w", encoding="utf-8") as f:
            for u in failed_users:
                f.write(f"{u}\n")

    print(f"\n✅ Done. Successfully added {added} members. Failed attempts saved in failed.txt\n")

async def main():
    while True:
        print("\n--- Spider Calls Menu ---")
        print("1 - Transfer members from one group to another")
        print("2 - Exit")
        print("3 - Delete current session and log in with another number")

        choice = input("Choose an option: ")

        if choice == "1":
            await transfer_members()
        elif choice == "2":
            print("Exiting...")
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
                print("✅ Session deleted. Restart the script to log in again.")
                break
            except Exception as e:
                print(f"❌ Error deleting session: {e}")
        else:
            print("❌ Invalid choice.")

with client:
    client.loop.run_until_complete(main())
