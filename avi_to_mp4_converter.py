"""
This converts our model's video predictions that are in format .AVI
to .MP4, where we can view them
"""

from moviepy.editor import *


def avi2mp4(clip_path, target_path):
    clip = VideoFileClip(clip_path)
    clip.write_videofile(target_path)

avi2mp4(clip_path='./runs/detect/predict2/drone.avi', target_path='./testing_video_results/drone_preds.mp4')