import pytube

link = input("Youtube Video URL")

video_donwload = pytube.YouTube(link)
video_donwload.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()

print(f"O video \"{link}\" foi baixado ")