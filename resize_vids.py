from moviepy.editor import VideoFileClip
import os

def resize_videos_in_folder(input_folder, target_width=640, target_height=360):
    # Check if the input folder exists
    if not os.path.exists(input_folder):
        print(f"The folder {input_folder} does not exist.")
        return

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        # Process only video files, you can add or modify extensions based on your requirements
        if os.path.isfile(file_path) and filename.lower().endswith(('.mp4', '.mov', '.avi')):
            print(f"Resizing video: {filename}")
            
            # Load the video
            clip = VideoFileClip(file_path)
            
            # Resize the video
            resized_clip = clip.resize(newsize=(target_width, target_height))
            
            # Replace the original video with the resized video
            # Make sure to back up your videos or work on copies if you don't want to lose the original resolution
            output_file_path = file_path  # This will overwrite the original video
            resized_clip.write_videofile(output_file_path, codec='libx264', audio_codec='aac')
            
            # Close the video file to free up resources
            clip.close()
            resized_clip.close()

    print("Finished resizing all videos.")

# Specify the path to your folder containing videos
input_folder = '/lfs/mercury1/0/willyc/watchdog/watchdog/unzipped/real_videos'
resize_videos_in_folder(input_folder)
