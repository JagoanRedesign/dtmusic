import os
import future
import asyncio
import requests
import wget
import time
import yt_dlp
from urllib.parse import urlparse
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from DAXXMUSIC import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch
from youtubesearchpython import SearchVideos



from pyrogram import Client, filters, types as t


@app.on_message(filters.regex("^https://www.instagram.com/"))
async def media_downloader(_,m: t.Message):
    if m.url is None or m.platform is None:
        return
    output = await DownloadMedia(m.platform,m.url)
    if output is None or output['code'] != 2 :
        return await m.reply_text("Unable to download media.")
    buildMedia = []
    for media in output['content']:
        if 'type' in media:
            if media['type'] in ["image","photo"]:
                buildMedia.append(t.InputMediaPhoto(media['url']))
            elif media['type'] == "video":
                buildMedia.append(t.InputMediaVideo(media['url']))
        else:
            mediaType = getContentType(media['url'])
            if mediaType in ["image","photo"]:
                buildMedia.append(t.InputMediaPhoto(media['url']))
            elif mediaType == "video":
                buildMedia.append(t.InputMediaVideo(media['url']))
    if len(buildMedia) == 0:
        return await m.reply_text("Unable to download media.")
    await m.reply_media_group(
        buildMedia,
        reply_to_message_id=m.id
    )
    return
