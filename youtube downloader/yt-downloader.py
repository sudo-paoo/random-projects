import youtube_dl
import re
import os
links = []
# url validator
def youtube_url_validation(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return youtube_regex_match

    return youtube_regex_match
#downloads in mp4 
def download_mp4(url):
    for yt_url in url:
        video_url = yt_url
        video_info = youtube_dl.YoutubeDL().extract_info(
            url=video_url, download = False
            )
        file = f"{video_info['title']}"
        options={
            'format':'bestvideo+bestaudio',
            'outtmpl':f"./downloads/mp4/{file}", # you can change the file location
            'ffmpeg-location': './'
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        print(f"Download Success: {file}")
        os.system("pause")
#downloads in mp3 format
def download_mp3(url):
    for yt_url in url:
        video_url = yt_url
        video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
        filename = f"{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':f"./downloads/mp3/{filename}" # you can change the file location
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        print(f"Download Success: {filename}")
        os.system("pause")

while True:
    link = input('Youtube URL: ')
    validator = youtube_url_validation(link)
    if str.lower(link) == 'mp4':
        for i in links:
            print("The following urls will be downloaded")
            print(f"URL: {i}")
        download_mp4(links)
        break
    elif str.lower(link) == 'mp3':
        for i in links:
            print("The following urls will be downloaded")
            print(f"URL: {i}")
        download_mp3(links)
        break
    elif link != 'mp4' or 'mp3':
        if validator:
            links.append(link)
            print(f"Valid URL.")
        else:
            print(f"Invalid URL.")
