import yt_dlp

SAVE_PATH = "D:/"

link = "youtube_url"

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Download best video and audio, fallback to best single format
    'outtmpl': f'{SAVE_PATH}%(title)s.%(ext)s',  # Save with title as the filename
    'merge_output_format': 'mp4',  # Ensure the final output is in mp4 format
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Convert the video to mp4 if it's in another format
    }],
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print('Video downloaded and merged successfully!')
except Exception as e:
    print(f"An error occurred: {e}")
