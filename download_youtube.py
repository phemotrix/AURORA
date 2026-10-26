"""
Aurora Music - Automated YouTube Music & Playlist Downloader
Downloads YouTube videos or full playlists as high-bitrate MP3s with embedded
cover artwork and ID3 metadata tags directly into your offline music folder.
"""

import os
import sys
import subprocess

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "my-music")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def ensure_yt_dlp():
    try:
        import yt_dlp
        return True
    except ImportError:
        print("📦 Installing yt-dlp for high-speed YouTube audio extraction...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"])
        print("✓ yt-dlp installed successfully!\n")
        return True

def download_audio(url):
    import yt_dlp

    print(f"\n🎵 Starting download from: {url}")
    print(f"📁 Destination folder: {OUTPUT_DIR}\n")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(OUTPUT_DIR, '%(artist,channel)s - %(title)s.%(ext)s'),
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            },
            {
                'key': 'FFmpegMetadata',
                'add_metadata': True,
            },
            {
                'key': 'EmbedThumbnail',
            }
        ],
        'writethumbnail': True,
        'prefer_ffmpeg': True,
        'quiet': False,
        'no_warnings': True,
        'ignoreerrors': True,
    }

    # If ffmpeg is not installed on the system, yt-dlp can still save the best audio directly (m4a/webm/opus)
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Notice: Standard postprocessor fallback: {e}")
        # Simplified fallback without ffmpeg postprocessing if ffmpeg is missing
        fallback_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
            'writethumbnail': True,
        }
        with yt_dlp.YoutubeDL(fallback_opts) as ydl:
            ydl.download([url])

    print("\n" + "="*60)
    print("✨ Download complete!")
    print(f"👉 Now open Aurora Music in your browser, click 'Upload Folder', and select:")
    print(f"   {OUTPUT_DIR}")
    print("="*60 + "\n")

if __name__ == '__main__':
    ensure_yt_dlp()

    if len(sys.argv) > 1:
        target_url = sys.argv[1]
    else:
        print("="*60)
        print("🌌 Aurora Music — YouTube Link Downloader")
        print("="*60)
        target_url = input("Enter YouTube Song or Playlist URL: ").strip()

    if target_url:
        download_audio(target_url)
    else:
        print("No URL provided. Exiting.")
