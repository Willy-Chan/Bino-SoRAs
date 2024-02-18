import cv2
import os

def process_video(video_path, output_base_path):
    # Open the video file
    vidcap = cv2.VideoCapture(video_path)
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    
    frame_width = int(vidcap.get(3))
    frame_height = int(vidcap.get(4))
    frame_rate = vidcap.get(cv2.CAP_PROP_FPS)  # Use original frame rate
    
    # # Prepare the output directory for extracted frames
    # frames_dir = os.path.join(output_base_path, f"{video_name}_frames")
    # os.makedirs(frames_dir, exist_ok=True)
    
    # Prepare the output video file
    new_video_path = os.path.join(output_base_path, f"{video_name}_processed.mp4")
    out = cv2.VideoWriter(new_video_path, cv2.VideoWriter_fourcc(*'MP4V'), frame_rate, (frame_width, frame_height))
    
    count = 0
    frame_list = []
    
    # Read through video frames
    success, image = vidcap.read()
    while success:
        if count % 8 == 0:  # Extract every 8th frame
            frame_list.append(image)
        
        success, image = vidcap.read()
        count += 1
    
    # Write selected frames to the output video
    for frame in frame_list:
        out.write(frame)
    
    # Release resources
    out.release()
    vidcap.release()

def process_folder(folder_path):
    output_base_path = 'processed_videos'
    os.makedirs(output_base_path, exist_ok=True)
    
    # Process each video file in the folder
    # filename = os.listdir(folder_path)[0]
    # if filename.lower().endswith(('.mp4', '.avi', '.mov')):  # Check for video file extensions
    #     video_path = os.path.join(folder_path, filename)
    #     process_video(video_path, output_base_path)


    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.mp4', '.avi', '.mov')):  # Check for video file extensions
            video_path = os.path.join(folder_path, filename)
            process_video(video_path, output_base_path)

# Specify your videos folder here
videos_folder = 'Sora/Sora'
process_folder(videos_folder)
