from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
def download_video(url,save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res_streams = streams.get_highest_resolution()
        highest_res_streams.download(output_path=save_path)
        print("Video downloaded successfully")

    except Exception as e:
        print(e)

url= "https://www.youtube.com/watch?v=svDWD_Matfg"
save_path="C:/Users/abhij/OneDrive/Desktop/Python Questions"
download_video(url,save_path)

# from sys import argv
# link = argv[1]
# yt = YouTube(link)

# print("Title: ",yt.title)
# print("View: ",yt.views)

# yd = yt.streams.get_highest_resolution()

# yd.download('C:/Users/abhij/Downloads/Video')

# link = YouTube("https://www.youtube.com/watch?v=svDWD_Matfg")
# video = link.streams.get_highest_resolution()

# video.download