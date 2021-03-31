from pytube import YouTube

def myapp():
    link = str(input('Link: '))
    if link != '':
        download_video(link)
    if link == 'QUIT' or 'quit' or 'Quit':
        quit()
    else:
        print('Enter something...\n')
        link = str(input('Link: '))

def download_video(link):
    video = YouTube(link)
    video_author = str(video.author)
    directory = str(input('Enter directory for video to be saved in: '))
    video.streams.first().download(directory, video_author)
    myapp()

if __name__ == '__main__':
    print()
    print('Youtube video downloader is running... Type QUIT to quit\n')
    myapp()