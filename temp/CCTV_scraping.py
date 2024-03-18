import os
import re
import warnings

import requests
import yt_dlp
from lxml import etree

warnings.filterwarnings("ignore", category=DeprecationWarning)


def download_video(url, output_folder):
    ydl_opts = {
        "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def judge(page_js):
    pattern = r'"url":"(.*?)"'
    result = re.search(pattern, page_js)
    if result:
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        return result.group(1).replace("\/", "/")
    return None


lose_name = []


def work(file_path):
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip()
            url = (
                "https://api.cntv.cn/NewVideo/getVideoListByColumn?id=TOPC1451558858788377&n=100&sort=desc&p=1&bd="
                + data
                + "&mode=2&serviceId=tvcctv&cb=cb"
            )
            resp = requests.get(url=url)
            page_js = resp.content.decode("unicode_escape")
            page_js_work = judge(page_js)
            output_file = "Y:/SignGPT/data/online/CCTV"
            print(url)
            try:
                download_video(page_js_work, output_file)
            except:
                lose_name.append(page_js_work)
                continue


with open("CCTV_lose.txt", "w", encoding="utf-8") as f:
    for name in lose_name:
        f.write(name + "\n")

txt_file = "E:/temp/data.txt"
video_urls = work(txt_file)
