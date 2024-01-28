import os
import time

def display_text_art(frame_folder, width, height, delay):
    for i in range(len(os.listdir(frame_folder))):
        frame_path = f"{frame_folder}/text_art{i:04d}.txt"
        with open(frame_path, "r", encoding="utf-8") as file:
            frame_content = file.read()
            os.system('cls' if os.name == 'nt' else 'clear')  # コンソールのクリア
            print(frame_content)
            time.sleep(delay)

if __name__ == "__main__":
    frame_folder = "frames"
    width = 100
    height = 50
    delay = 0.01  # 各フレームの表示時間（秒）

    display_text_art(frame_folder, width, height, delay)
