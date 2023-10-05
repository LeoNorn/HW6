from email import message

from bot import bot

ban_words = ["гнида", "засранец", "идиот", "ублюдок", "офигевший"]

for word in ban_words:
    if word in message.text.lower().replace(" ", ""):
        await bot.delete_message(
            chat_id=message.chat.id,
            message_id=message.message_id
        )

        await bot.send_message(
            chat_id=message.chat.id,
            text=f"Плохой мальчик, {message.from_user.username}!"
        )