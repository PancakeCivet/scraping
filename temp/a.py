import os

import yt_dlp


def download_video(url, output_folder):
    ydl_opts = {
        "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


output_file = "Y:/SignGPT/data/online/BiLiBiLi"
"""for i in range(1, 8, 1):
    url = "https://hk4-edge27-1.edgeware.tvb.com/session/df3e6c06-e454-11ee-a57b-0050569023d7/wbypsa/newsbksdrm/_definst_/smil:news/inews1/20240316/archive_117245_775807_1280_720_1500k_cht_proenv_can.smil/segment_ctvideo_ridp0va0br1228920_cs2700000_mpd.m4s"
    try:
        download_video(url, output_file)
    except:
        continue"""

# python -u "e:\temp\a.py"
"""
https://hk4-edge27-1.edgeware.tvb.com/session/df3e6c06-e454-11ee-a57b-0050569023d7/wbypsa/newsbksdrm/_definst_/smil:news/inews1/20240316/archive_117245_775807_1280_720_1500k_cht_proenv_can.smil/segment_ctvideo_ridp0va0br1228920_cs3600000_mpd.m4s
https://hk4-edge27-1.edgeware.tvb.com/session/df3e6c06-e454-11ee-a57b-0050569023d7/wbypsa/newsbksdrm/_definst_/smil:news/inews1/20240316/archive_117245_775807_1280_720_1500k_cht_proenv_can.smil/segment_ctvideo_ridp0va0br1228920_cs2700000_mpd.m4s
"""

url = "https://news.tvb.com/tc/programme/newsreportwithsignlanguage/65f597937a651a5efac7cdf9/%E6%89%8B%E8%AA%9E%E6%96%B0%E8%81%9E%E5%A0%B1%E9%81%93-%E6%89%8B%E8%AA%9E%E6%96%B0%E8%81%9E%E5%A0%B1%E9%81%93"
download_video(url, output_file)
