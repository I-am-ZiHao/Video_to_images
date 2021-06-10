import os.path
import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser(description='Convert frames into a video')
parser.add_argument('--frames', default='/path/to/images', type=str, help='video frames file')
parser.add_argument('--output', default='video', type=str, help='output video name')
parser.add_argument('--fps', default=25, type=int, help='fps of output video')
parser.add_argument('--resize', dest='resize', help='resize the frame if it is too large', action='store_true')

def main():
    args = parser.parse_args()
    frames_name= os.listdir(args.frames)
    frames_name.sort()  
    fps = args.fps
    out = 0
    count = 0
    for frame_name in frames_name:
        print('Processing', frame_name, '...')
        path = os.path.join(args.frames, frame_name)
        frame = cv2.imread(path)
        h, w, _ = frame.shape

        if args.resize:
            size = (int(w / 2), int(h / 2))
            frame = cv2.resize(frame, size, interpolation=cv2.INTER_CUBIC)
        else:
            size = (w, h)
        
        if count == 0:
            out = cv2.VideoWriter(args.output + '.mp4',cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
            count += 1
        out.write(frame)
    out.release()

if __name__ == '__main__':
    main()