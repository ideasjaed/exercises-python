import pytube

video_url = input("Inserte URL del video: ")
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download(r'D:\Documentos\DescargasPythonVideo')