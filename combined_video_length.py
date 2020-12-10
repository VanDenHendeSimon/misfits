from moviepy.editor import VideoFileClip
import os
import datetime


def main():
    input_dir = input("input dir >> ")
    total_duration = 0

    for f in os.listdir(input_dir):
        if os.path.splitext(f)[1] == ".mp4":
            clip = VideoFileClip(os.path.join(input_dir, f))
            print(f)
            total_duration += clip.duration

    print(datetime.timedelta(seconds=total_duration))


if __name__ == '__main__':
    main()
