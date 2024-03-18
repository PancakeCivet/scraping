import os
import shutil


def move_mp4_files(source_folder, dest_folder):
    # 确保目标文件夹存在
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 遍历源文件夹中的所有文件
    for file_name in os.listdir(source_folder):
        source_path = os.path.join(source_folder, file_name)

        # 如果是文件并且扩展名为 .mp4，则移动到目标文件夹
        if os.path.isfile(source_path) and file_name.endswith(".mp4"):
            dest_path = os.path.join(dest_folder, file_name)
            shutil.move(source_path, dest_path)
            print(f"Moved {file_name} to {dest_folder}")


if __name__ == "__main__":
    # 替换为实际的源文件夹和目标文件夹路径
    source_folder = "E:/youtubeasl/videos"
    dest_folder = "Y:/SignGPT/data/online/youtubeasl"

    while 1:
        move_mp4_files(source_folder, dest_folder)
