from pytube import YouTube


def get_video_info(video_url):
    video = YouTube(video_url)
    print("Название видео:", video.title)
    print("Автор:", video.author)
    print("Длительность:", video.length, "секунд")

    return video.watch_url

