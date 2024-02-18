import cv2
import os

def extract_5_second_clips(video_path, output_dir):
    # Create a subfolder in the output directory named after the video file
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    video_output_dir = os.path.join(output_dir, video_name)
    if not os.path.exists(video_output_dir):
        os.makedirs(video_output_dir)

    vidcap = cv2.VideoCapture(video_path)
    frame_rate = vidcap.get(cv2.CAP_PROP_FPS)  # Get the frame rate of the video
    duration_in_frames = int(5 * frame_rate)  # Calculate the duration of 5 seconds in frames

    success, image = vidcap.read()
    count = 0

    # Extract and save frames up to the 5-second mark, skipping every 8th frame
    while success and count < duration_in_frames:
        frame_filename = f"frame{count:06d}.jpg"
        cv2.imwrite(os.path.join(video_output_dir, frame_filename), image)
        success, image = vidcap.read()
        count += 1

    vidcap.release()

def process_folder(input_folder, output_folder):
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        print(filename)
        file_path = os.path.join(input_folder, filename)
        # Check if the file is a video (adjust extensions as needed)
        if os.path.isfile(file_path) and filename.lower().endswith(('.mp4', '.avi', '.mov')):
            print(f"Processing {filename}...")
            extract_5_second_clips(file_path, output_folder)

# Specify the paths to your input and output folders
input_folder = '/lfs/mercury1/0/willyc/watchdog/watchdog/REALVIDS'
output_folder = '/lfs/mercury1/0/willyc/watchdog/watchdog/REALVIDS_FRAMES'

process_folder(input_folder, output_folder)
