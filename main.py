import cv2
import os

video_path = 'video/sampleVid.mp4'
vidcap = cv2.VideoCapture(video_path)

new_video_path = 'inputVid/selectedFramesVideo.mp4'
frame_width = int(vidcap.get(3))
frame_height = int(vidcap.get(4))
# Adjust the frame rate according to the number of frames you're skipping
frame_rate = vidcap.get(cv2.CAP_PROP_FPS) / 8
out = cv2.VideoWriter(new_video_path, cv2.VideoWriter_fourcc(*'MP4V'), frame_rate, (frame_width, frame_height))

extracted_frames_dir = 'extracted_frames'
interpolated_frames_dir = 'interpolated_frames'
os.makedirs(extracted_frames_dir, exist_ok=True)
os.makedirs(interpolated_frames_dir, exist_ok=True)

success, image = vidcap.read()
count = 0

while success:
    if count % 8 == 0:  # Process every 8th frame
        # Save frame for the new video
        out.write(image)
        # Save the frame as a JPEG file
        cv2.imwrite(f"{extracted_frames_dir}/frame{count}.jpg", image)
    success, image = vidcap.read()
    count += 1

out.release()
vidcap.release()
