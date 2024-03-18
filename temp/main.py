import os

import yt_dlp


def download_video(url, output_folder):
    ydl_opts = {
        "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


"""
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=aoLQ0VchSec"
    output_file = "E:/youtubeasl/"

    download_video(video_url, output_file)
"""


def extract_urls_from_file(file_path):
    with open(file_path, "r") as file:
        urls = set()
        for line in file:
            url = line.strip()
            if url:
                urls.add("https://www.youtube.com/watch?v=" + url)
        return urls


# 正式代码

lose = 0
lose_name = []

txt_file = "E:/temp/youtube-asl_youtube_asl_video_ids.txt"
video_urls = extract_urls_from_file(txt_file)
output_file = "Y:\SignGPT\data\online\youtubeasl"
for url in video_urls:
    try:
        download_video(url, output_file)
    except:
        lose = lose + 1
        lose_name.append(url)
        continue
# 测试

"""txt_file = "E:/youtubeasl/text.txt"
video_urls = extract_urls_from_file(txt_file)
output_file = "E:/youtubeasl/videos_text"
for url in video_urls:
    download_video(url, output_file)
"""
