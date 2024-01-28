from PIL import Image
import cv2
import os

# 動画ファイルからフレームを抽出する
def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_path = f"{output_folder}/frame{count:04d}.png"
        cv2.imwrite(frame_path, frame)

        count += 1

    cap.release()

# 画像をテキストアートに変換する
def image_to_text_art(image_path, output_text_path, width, height):
    image = Image.open(image_path).convert("L")
    image = image.resize((width, height))

    ascii_chars = "@%#*+=-:. "

    pixels = image.getdata()
    ascii_str = ""

    for pixel_value in pixels:
        pixel_value = max(0, min(pixel_value, 255))
        index = int(pixel_value * len(ascii_chars) / 256)
        ascii_str += ascii_chars[index]

    with open(output_text_path, "w") as text_file:
        for i in range(0, len(ascii_str), width):
            text_file.write(ascii_str[i:i+width] + "\n")

# メイン関数
def main():
    video_path = "./badapple.mp4"
    output_folder = "frames"
    output_text_path = "output_text.txt"
    width = 100
    height = 50

    # 動画からフレームを抽出
    extract_frames(video_path, output_folder)

    # フレームごとにテキストアートに変換して保存
    for i in range(len(os.listdir(output_folder))):
        frame_path = f"{output_folder}/frame{i:04d}.png"
        image_to_text_art(frame_path, f"{output_folder}/text_art{i:04d}.txt", width, height)

if __name__ == "__main__":
    main()
