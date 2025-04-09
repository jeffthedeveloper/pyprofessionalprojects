import requests
import youtube_dl

def baixar_podcast(url, arquivo_destino):
    response = requests.get(url)
    with open(arquivo_destino, "wb") as f:
        f.write(response.content)

def baixar_video_youtube(url, pasta_destino):
    ydl_opts = {"outtmpl": f"{pasta_destino}/%(title)s.%(ext)s"}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

baixar_podcast("URL_PODCAST", "podcast.mp3")
baixar_video_youtube("URL_VIDEO_YOUTUBE", "videos")