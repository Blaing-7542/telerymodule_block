from pyrogram import Client, filters
import uuid

cinfo = "⛔`block`"
ccomand = " блокирует пользователя (работает только в личных сообщениях)"
with open("userbot.info", "r") as file:
    lines = file.readlines()
    prefix_userbot = lines[2].strip()


def command_block(app):
    @app.on_message(filters.me & filters.command("block", prefixes=prefix_userbot))
    def block_user(client, message):
        user_id = message.chat.id
        user_name = message.chat.username
        message.edit(f"**{user_name} заблокирован.**")
        client.block_user(user_id)

print("Модуль block загружен!")
