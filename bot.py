import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters

BOT_TOKEN = os.getenv("7785136840:AAHn3Ft4RqxXutG38nelgrHlDEz6eUvLNto")
ADMIN_CHAT_ID = int(os.getenv("1209078214")) 

async def receive_question(update, context):
    question_text = update.message.text

    # Send ONLY the question (anonymous)
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"❓ New Anonymous Question:\n\n{question_text}"
    )

    # Confirmation to user
    await update.message.reply_text(
        "Your question has been sent **anonymously**. 👍"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_question))
    app.run_polling()

if __name__ == "__main__":
    main()
