from DAXXMUSIC import app
from pyrogram import filters
from pyrogram import Client, filters

from pyrogram import Client, filters, types as t
from pytube import YouTube
import os


# Fungsi untuk mengunduh video dari Facebook
def download_facebook_video(url):
    yt = YouTube(url)
    video = yt.streams.filter(file_extension='mp4').first()
    return video

# Handler untuk pesan yang mengandung URL Facebook
@app.on_message(filters.regex("^https://www.facebook.com/"))
async def media_downloader(_, m: t.Message):
    if "facebook" in m.text.lower():
        video = download_facebook_video(m.text)
        if video:
            video_path = video.download()
            await m.reply_video(video_path, reply_to_message_id=m.message_id)
            os.remove(video_path)
        else:
            await m.reply_text("Gagal mengunduh video dari Facebook")
    else:
        # Proses untuk mengunduh media dari platform lain (disesuaikan)
        pass
