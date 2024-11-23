# Download High-Quality Video from YouTube

This Python script uses `yt-dlp` to download high-quality videos from YouTube. It supports downloading videos in various resolutions and formats, including audio-only downloads. The script leverages FFmpeg for post-processing tasks like format conversion and merging video/audio streams.

## Features
- Download videos in multiple resolutions.
- Supports audio-only downloads.
- FFmpeg integration for advanced post-processing.
- Simple command-line interface.

## Requirements
- Python 3.x
- `yt-dlp` library
- FFmpeg (for post-processing)

## Installation

Clone this repository:

```bash
git clone https://github.com/superbabii/Download-high-quality-video-from-YouTube.git
```

Install the required dependencies:

```bash
pip install yt-dlp
```

### FFmpeg Setup

Download and install FFmpeg from [FFmpeg.org](https://ffmpeg.org/download.html). Add the FFmpeg binary to your system's PATH:

- **Windows:** Add the path to `ffmpeg.exe` in the Environment Variables under `System Properties > Advanced > Environment Variables`.
- **macOS/Linux:** Add the following line to your `.bashrc` or `.zshrc`:
  ```bash
  export PATH="$PATH:/path/to/ffmpeg"
  ```

## Usage

1. Open the `main.py` script in a text editor.

2. Replace the placeholder string `"youtube_url"` with the actual YouTube URL you want to download:

   ```python
   youtube_url = "https://www.youtube.com/watch?v=your_video_id"
   ```

3. Save the file.

4. Run the script:

   ```bash
   python main.py
   ```

The video will be downloaded and processed by FFmpeg in the current directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
