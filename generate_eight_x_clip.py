import cv2
import os

def frames_to_video(subfolder_path, output_folder, frame_rate):
    video_name = os.path.basename(subfolder_path)
    output_file = os.path.join(output_folder, f"{video_name}.mp4")
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # For an .mp4 output file
    video_writer = None

    # Sort files to ensure correct order
    files = [f for f in os.listdir(subfolder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    files.sort()

    for file in files:
        print(file)
        frame_path = os.path.join(subfolder_path, file)
        image = cv2.imread(frame_path)
        
        # Initialize video writer with the first frame's size
        if video_writer is None:
            height, width, layers = image.shape
            video_writer = cv2.VideoWriter(output_file, fourcc, frame_rate, (width, height))

        video_writer.write(image)

    # Release the video writer
    if video_writer is not None:
        video_writer.release()

def process_subfolders(input_folder, output_folder, frame_rate):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each subfolder in the input folder
    for subfolder in next(os.walk(input_folder))[1]:
        subfolder_path = os.path.join(input_folder, subfolder)
        print(f"Processing {subfolder}...")
        frames_to_video(subfolder_path, output_folder, frame_rate)
    
    print("All videos have been created.")

# Specify the paths and frame rate
input_folder = '/lfs/mercury1/0/willyc/watchdog/watchdog/B1/big-sur_processed_8x'
output_folder = '/lfs/mercury1/0/willyc/watchdog/watchdog/B2'
frame_rate = 30  # Adjust frame rate as needed

process_subfolders(input_folder, output_folder, frame_rate)
