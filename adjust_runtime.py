from moviepy.editor import VideoFileClip
import os

def adjust_runtimes(original_folder, processed_folder):
    # Iterate over files in the processed folder
    for processed_file in os.listdir(processed_folder):
        if processed_file.endswith("_processed_8x.mp4"):  # Assuming MP4 format for simplicity
            # Construct the original file name by removing '_processed' from the name
            original_file_name = processed_file.replace("_processed_8x", "")
            original_file_path = os.path.join(original_folder, original_file_name)
            processed_file_path = os.path.join(processed_folder, processed_file)

            # Check if the original file exists
            if os.path.exists(original_file_path):
                # Load both video clips
                original_clip = VideoFileClip(original_file_path)
                processed_clip = VideoFileClip(processed_file_path)

                # Calculate the runtime difference
                difference = original_clip.duration - processed_clip.duration

                # Clip off the difference from the original and create a new clip
                if difference > 0:
                    new_clip = original_clip.subclip(0, max(0, original_clip.duration - difference))
                    # Overwrite the original file with the new clip
                    new_clip.write_videofile(original_file_path, codec="libx264", audio_codec="aac")
                else:
                    print(f"No clipping required for {original_file_name}.")

                # Release resources
                original_clip.close()
                processed_clip.close()
            else:
                print(f"Original file {original_file_name} does not exist in the original folder.")

# Specify the paths to your folders
original_folder = '/lfs/mercury1/0/willyc/watchdog/watchdog/Sora/Sora'
processed_folder = '/lfs/mercury1/0/willyc/watchdog/watchdog/interpolated_vids'

adjust_runtimes(original_folder, processed_folder)
