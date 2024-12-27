# src/downloader.py
from pytube import YouTube, Playlist

def download_youtube_video(url, resolution):
    """
    Downloads a YouTube video at the specified resolution.
    
    Parameters:
    url (str): The URL of the YouTube video.
    resolution (str): The desired resolution (e.g., '1080p', '720p').
    """
    try:
        yt = YouTube(url)
        video = yt.streams.filter(res=resolution, file_extension='mp4').first()
        if video:
            video.download()
            print(f"Downloaded video: {yt.title} at resolution: {resolution}")
        else:
            print(f"No stream available at resolution: {resolution}, attempting highest available resolution.")
            video = yt.streams.get_highest_resolution()
            video.download()
            print(f"Downloaded video: {yt.title} at highest available resolution.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

def download_youtube_playlist(url, resolution):
    """
    Downloads all videos in a YouTube playlist at the specified resolution.
    
    Parameters:
    url (str): The URL of the YouTube playlist.
    resolution (str): The desired resolution for the videos.
    """
    try:
        pl = Playlist(url)
        print(f"Downloading playlist: {pl.title}")
        for video_url in pl.video_urls:
            download_youtube_video(video_url, resolution)
        print("All videos in the playlist have been downloaded.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function to interact with the user and download videos or playlists.
    """
    url = input("Please enter the URL of the YouTube video or playlist you want to download: ")
    choice = input("Is this link a single video or a playlist? (Enter 'video' or 'playlist'): ").strip().lower()
    resolution = input("Enter the desired resolution (e.g., 1080p, 720p, 480p): ").strip().lower()

    if choice == 'video':
        download_youtube_video(url, resolution)
    elif choice == 'playlist':
        download_youtube_playlist(url, resolution)
    else:
        print("Invalid choice. Please enter either 'video' or 'playlist'.")

if __name__ == "__main__":
    main()
