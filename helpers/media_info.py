from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from urllib.parse import quote_plus, unquote
from helpers.download_from_url import download_file, get_size
from helpers.file_handler import send_to_transfersh_async, progress
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from helpers.display_progress import progress_for_pyrogram, humanbytes
import os, math, time, datetime, aiohttp, asyncio, mimetypes,logging
from helpers.tools import execute
from helpers.ffprobe import stream_creator
from helpers.thumbnail_video import thumb_creator

logger = logging.getLogger(__name__)

async def cinfo2(bot , m):
   
   ft = m.audio or m.video or m.document
   fsize = get_size(ft.file_size)
   if ft.mime_type and ft.mime_type.startswith("audio/"):
      if ft.file_name:
         fn = str(ft.file_name)
      else:
         fn = "šš¢š„š š§šš¦š š§šØš­ ššš­ššš­šš!"
      if m.document:
         #await m.reply_text(text=f"š šš¢š§š¤ š¢š§ššØ:\n\nšš¢š„š: {cfname}\nMime-Type: {mt}\nšš¢š³š: {url_size}\n\nšš¬š /upload šš¬ š«šš©š„š² š­šØ š²šØš®š« š„š¢š§š¤, š­šØ š®š©š„šØšš š²šØš®š« š„š¢š§š¤ š­šØ š­šš„šš š«šš¦.\n\nššš /help.", quote=True)
         await m.reply_text(text=f"š šššš¢š š¢š§ššØ:\n\nšš¢š„š: {fn}\nMime-Type: {ft.mime_type}\nšš¢š³š: {fsize}\n\nšš¬š /rna š­šØ š«šš§šš¦š šš§š ššš¢š­ šš®šš¢šØ š­šš š¬.\n\nššš /help.", quote=True)
         return
      if m.audio.title:
         tt = str(ft.title)
      else:
         tt = "šš¢š­š„š š§šØš­ ššš­ššš­šš!"
      if m.audio.performer:
         pf = str(ft.performer)
      else:
         pf = "ššØ šš«š­š¢š¬š­(š¬) ššš­ššš­šš!"
      await m.reply_text(text=f"š šššš¢š š¢š§ššØ:\n\nšš¢š„š: {fn}\nMime-Type: {ft.mime_type}\nšš¢š­š„š: {tt}\nšš«š­š¢š¬š­: {pf}\nSize: {fsize}\n\nUse /rna to rename and edit audio tags.\n\nSee /help.", quote=True)
   elif ft.mime_type and ft.mime_type.startswith("video/"):
      if ft.file_name:
         fn = str(ft.file_name)
      else:
         fn = "ššØ šš¢š„š š§šš¦š ššš­ššš­šš!"
      await m.reply_text(text=f"š šššš¢š š¢š§ššØ:\n\nšš¢š„š: {fn}\nMime-Type: {ft.mime_type}\nšš¢š³š: {fsize}\n\nšš¬š /c2v to convert or /rnv to rename this video.\n\nSee /help.", quote=True)
   else:
      if ft.file_name:
         fn = str(ft.file_name)
      else:
         fn = "ššØ šš¢š„š š§šš¦š ššš­ššš­šš!"
      await m.reply_text(text=f"š šššš¢š š¢š§ššØ:\n\nšš¢š„š: {fn}\nMime-Type: {ft.mime_type}\nšš¢š³š: {fsize}\n\nšš¬š /rnf to rename this file.\n\nSee /help.", quote=True)
