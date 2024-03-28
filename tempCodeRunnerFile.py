from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, url):
        '''
        initialise YouTubeDownloader object with provided url
        '''
        self.url=url
        self.youtube_video=YouTube(self.url)
    
    def video_info(self):
        '''
        prints informationn about the YouTube video
        '''
        print("Title:", self.youtube.title)
        print("Views:", self.youtube.views)
    
    def download_video(self,path):
        '''
        download the video to the specified path
        '''
        download_video=self.youtube_video.streams.get_highest_resolution()
        print('Downloading...')
        download_video.download(path)
        print('Download complete!')

def main():
    url=input('Paste the YouTube video URL: ')
    path='C:/Users/DELL/Downloads'
    downloader=YouTubeDownloader(url)
    downloader.video_info()
    downloader.download_video(path)

if __name__ == "__main__":
    main()