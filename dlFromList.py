from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv

# class MyLogger(object):
#     def debug(self, msg):
#         pass
#
#     def warning(self, msg):
#         pass
#
#     def error(self, msg):
#         print(msg)


# def my_hook(d):
#     if d['status'] == 'finished':
#         print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'outtml': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    # 'logger': MyLogger(),
    # 'progress_hooks': [my_hook],
}

if not os.path.exists('Songs'):
    os.mkdir('Songs')
os.chdir('Songs')

if len(argv) < 1:
    raise IndexError('please enter file name')

with open('../' + argv[1], 'r') as f:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for song_url in f:
            ydl.download([song_url])