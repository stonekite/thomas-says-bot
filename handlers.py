from datetime import datetime, timedelta
from telegram.constants import PARSEMODE_HTML
from telegram import Update
from telegram.ext import CallbackContext
import requests


match_endpoint = "https://thomas-says-api.vercel.app/api/keyword/match"
last_sent = datetime.now() - timedelta(minutes=10)


def message_handler(update: Update, context: CallbackContext):
  global last_sent
  now = datetime.now()
  if now - last_sent < timedelta(minutes=10):
    return

  text = update.message.text
  quote = requests.post(match_endpoint, data={ "message": text }).json()

  if not quote:
    return

  quote_message = f"""\"{quote["text"]}\"
- <i>{quote["authorName"]}</i>"""

  context.bot.send_message(
    text=quote_message,
    chat_id=update.effective_chat.id,
    reply_to_message_id=update.effective_message.message_id,
    parse_mode=PARSEMODE_HTML,
    disable_notification=True
  )

  last_sent = now
