import cv2
import argparse

parser = argparse.ArgumentParser(description='convert MP4 to video frames')
parser.add_argument('--video_path', type=str, help='video path')
parser.add_argument('--save_path', type=str, help='path for output video frames')

def main():
    args = parser.parse_args()
    vidcap = cv2.VideoCapture(args.video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(args.save_path + "/frame_%06d.jpg" % count, image)
        success, image = vidcap.read()
        print ('Read a new frame'+ str(count) +': ', success)
        count += 1

if __name__ == '__main__':
    main()