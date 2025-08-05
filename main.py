#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import AiVideoAnalyser

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from pathlib import Path
import yt_dlp

def download_audio_from_youtube(youtube_url, output_path="video.mp3"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    
    print(f"Downloaded audio to {output_path}")
    return output_path

def run():
    """
    Run the crew.
    """
    youtube_url = "https://youtu.be/1aA1WGON49E?si=2Kk0C7SDXPg4m6cD"
    output_path = download_audio_from_youtube(youtube_url)

    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year),
        'file_path': output_path
    }
    
    try:
        AiVideoAnalyser().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()


# from pathlib import Path
# SCRIPT_DIR = Path(__file__).parent 

# def run():
#     """
#     Run the crew.
#     """
#     inputs = {
#         'topic': 'AI LLMs',
#         'current_year': str(datetime.now().year),
#         'file_path': str(SCRIPT_DIR / "video.mp4")

#     }
    
#     try:
#         AiVideoAnalyser().crew().kickoff(inputs=inputs)
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")
# run()