import cv2
from glob import glob
import sys

def main():
    args = sys.argv
    print(args[1])
    dir_name = args[1]

    videos_path = glob(f'{dir_name}*.mov')
    total_time = 0

    for video_path in videos_path:
        cap = cv2.get(cv2.CAP_PROP_FPS)
        video_frame_count = cap.get(cv2.CAP_PROP_FNAME_COUNT)
        video_fps = cap.get(cv2.CAP_PROP_FPS)
        time = video_frame_count / video_fps
        total_time += time

        total_time = round(total_time/60/60, 2)
        print(f'合計金額:{total_time}')

if __name__ == "__main__":
    main()
