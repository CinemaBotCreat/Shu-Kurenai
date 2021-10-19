"""
MIT License

Copyright (C) 2021 Horimaya

This file is part of @@WolfXRobot(Telegram Bot)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import io
import requests
import shutil 
import random
import re
import glob
import time

from io import BytesIO
from requests import get
from telethon.tl.types import InputMessagesFilterPhotos

from Wolf-X import OWNER_ID, BOT_USERNAME, SUPPORT_CHAT
from wolf-X.events import register
from Wolf-X import telethn
from PIL import Image, ImageDraw, ImageFont


LOGO_LINKS            = ["https://telegra.ph/file/d1838efdafce9fe611d0c.jpg",
                         "https://telegra.ph/file/c1ff2d5ec5e1b5bd1b200.jpg",
                                                  "https://telegra.ph/file/08c5fbe14cc4b13d1de05.jpg",
                                                                           "https://telegra.ph/file/66614a049d74fe2a220dc.jpg",
                                                                                                    "https://telegra.ph/file/9cc1e4b24bfa13873bd66.jpg",
                                                                                                                             "https://telegra.ph/file/792d38bd74b0c3165c11d.jpg",
                                                                                                                                                      "https://telegra.ph/file/e1031e28a4aa4d8bd7c9b.jpg",
                                                                                                                                                                               "https://telegra.ph/file/2be9027c55b5ed463fc18.jpg",
                                                                                                                                                                                                        "https://telegra.ph/file/9fd71f8d08158d0cc393c.jpg",
                                                                                                                                                                                                                                 "https://telegra.ph/file/627105074f0456f42058b.jpg",
                                                                                                                                                                                                                                                          "https://telegra.ph/file/62b712f741382d3c171cd.jpg",
                                                                                                                                                                                                                                                                                   "https://telegra.ph/file/496651e0d5e4d22b8f72d.jpg",
                                                                                                                                                                                                                                                                                                            "https://telegra.ph/file/6619d0eee2c35e022ee74.jpg",
                                                                                                                                                                                                                                                                                                                                     "https://telegra.ph/file/f72fcb27c9b1e762d184b.jpg",
                                                                                                                                                                                                                                                                                                                                                              "https://telegra.ph/file/01eac0fe1a722a864d7de.jpg",
                                                                                                                                                                                                                                                                                                                                                                                       "https://telegra.ph/file/bdcb746fbfdf38f812873.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                "https://telegra.ph/file/d13e036a129df90651deb.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                         "https://telegra.ph/file/ab6715ce9a63523bd0219.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                  "https://telegra.ph/file/c243f4e80ebf0110f9f00.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           "https://telegra.ph/file/ff9053f2c7bfb2badc99e.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    "https://telegra.ph/file/00b9ebbb816285d9a59f9.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             "https://telegra.ph/file/ad92e1c829d14afa25cf2.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      "https://telegra.ph/file/58d45cc3374e7b28a1e67.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               "https://telegra.ph/file/4140a0b3f27c302fd81cb.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "https://telegra.ph/file/c4db2b5c84c1d90f5ac8a.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 "https://telegra.ph/file/c0da5080a3ff7643ddeb4.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          "https://telegra.ph/file/79fad473ffe888ed771b2.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   "https://telegra.ph/file/eafd526d9dcc164d7269f.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "https://telegra.ph/file/98b50e8424dd2be9fc127.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     "https://telegra.ph/file/c1ad29c189162a1404749.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              "https://telegra.ph/file/2d288450ebecc500addbd.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       "https://telegra.ph/file/9715353976a99becd7632.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                "https://telegra.ph/file/87670b02a1004bc02bd8d.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         "https://telegra.ph/file/70789cd69114939a78242.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  "https://telegra.ph/file/1566bd334f00645cfa993.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           "https://telegra.ph/file/9727c37bb8c633208b915.jpg",
@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
  if event.sender_id == OWNER_ID:
       pass
        else:
  if not quew:
       await event.reply('Please Gimmie A Text For The Logo.')
            return
             pesan = await event.reply('Logo In A Process. Please Wait.')
              try:
                  text = event.pattern_match.group(1)
                      randc = random.choice(LOGO_LINKS)
                          img = Image.open(io.BytesIO(requests.get(randc).content))
                              draw = ImageDraw.Draw(img)
                                  image_widthz, image_heightz = img.size
                                      pointsize = 500
                                          fillcolor = "black"
           
