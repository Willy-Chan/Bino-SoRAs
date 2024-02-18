import os
import shutil

def copy_frames_except_every_eighth(src_folder, dest_folder):
    # Check if the source folder exists
    if not os.path.exists(src_folder):
        print(f"The folder {src_folder} does not exist.")
        return

    # Ensure the destination folder exists
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Walk through all subfolders in the source folder
    for subdir, dirs, files in os.walk(src_folder):
        # Calculate relative path to create the same structure in the destination
        relative_path = os.path.relpath(subdir, src_folder)
        new_subdir = os.path.join(dest_folder, relative_path)

        # Ensure subdirectories exist in the destination folder
        if not os.path.exists(new_subdir):
            os.makedirs(new_subdir)

        # Sort files to maintain order
        files.sort()

        # Copy all files except every eighth starting from the first (index 0)
        for i, file in enumerate(files):
            if i % 8 != 0:  # Skip every eighth file
                src_file_path = os.path.join(subdir, file)
                dest_file_path = os.path.join(new_subdir, file)

                # Copy the file to the new location
                shutil.copy2(src_file_path, dest_file_path)

    print("Finished copying frames, skipping every eighth frame.")

# Specify the source and destination folders
src_folder = '/lfs/mercury1/0/willyc/watchdog/watchdog/real_frames'
dest_folder = '/lfs/mercury1/0/willyc/watchdog/watchdog/real_interpolated_frames'
copy_frames_except_every_eighth(src_folder, dest_folder)
