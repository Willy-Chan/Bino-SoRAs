import os

normal_folder = "./normal_frames"
interpolated_folder = "./interpolated_frames"
output_file = "fid_scores.txt"

with open(output_file, "a") as f:
    f.write("FID Scores:\n")

for folder in os.listdir(normal_folder):
    normal_path = os.path.join(normal_folder, folder)
    interpolated_path = os.path.join(interpolated_folder, folder + "_processed_8x")
    
    if os.path.isdir(normal_path) and os.path.isdir(interpolated_path):
        command = f"python -m pytorch_fid {normal_path}/ {interpolated_path}/"
        status_update = f"Calculating FID score for {folder}..."
        print(status_update)
        
        # Redirect output to file
        command_with_output_redirect = f"{command} >> {output_file} 2>&1"
        
        # Execute command
        os.system(command_with_output_redirect)
        
        # Append status update to file
        with open(output_file, "a") as f:
            f.write("\n" + "=" * len(status_update) + "\n")
            f.write(status_update + "\n")
            f.write("=" * len(status_update) + "\n")
    else:
        print(f"Corresponding pair not found for folder {folder}")