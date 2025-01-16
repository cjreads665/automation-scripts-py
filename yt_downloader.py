from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

url = "https://www.youtube.com/watch?v=zT7niRUOs9o&t=967s"

path = "."

def download_video(url,save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        streams.get_highest_resolution().download(save_path)
        print(f"video downloaded to {save_path}")
    except Exception as e:
        print(e)

download_video(url,path)