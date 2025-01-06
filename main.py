import re
import subprocess
import sys
import traceback
from gtts import gTTS
from inspect import getfullargspec
from io import StringIO
from time import time
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

API_ID = "16457832"
API_HASH = "3030874d0befdb5d05597deacc3e83ab"
BOT_TOKEN = "7882393332:AAGb4-Y6JGWeTb1h58-jf8jtXzi8nowPkJ0 "

app = Client(
           name="EVAL", 
           api_id=API_ID, 
           api_hash=API_HASH, 
           bot_token=BOT_TOKEN
)

@app.on_message(filters.command("tts"))
async def text_to_speech(client, message):
    # Extract text from the command or the replied message
    text = None

    if len(message.command) > 1:
        # If the command has additional text, use it
        text = message.text.split(' ', 1)[1]
    elif message.reply_to_message and message.reply_to_message.text:
        # If replying to a message with text, use that text
        text = message.reply_to_message.text

    if not text:
        await message.reply_text("Usage: `/tts4 <text>` or reply to a text message with `/tts4`.")
        return

    try:
        # Generate TTS audio
        tts = gTTS(text=text, lang='pa')
        audio_file = 'BADUSERBOT_audio.mp3'
        tts.save(audio_file)
        
        # Send the audio file
        await message.reply_audio(audio_file)
    except Exception as e:
        # Handle errors
        await message.reply_text(f"An error occurred: {str(e)}")
    finally:
        # Clean up the saved audio file
        if os.path.exists(audio_file):
            os.remove(audio_file)

if __name__ == "__main__":
    app.run()
