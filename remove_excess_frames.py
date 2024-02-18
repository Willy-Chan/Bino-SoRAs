import os

def remove_excess_frames(folder1, folder2):
    # Iterate over subfolders in the first folder
    for subfolder in os.listdir(folder1):
        print(subfolder)
        subfolder_path1 = os.path.join(folder1, subfolder)
        subfolder_path2 = os.path.join(folder2, subfolder)

        # Ensure the subfolder exists in both main folders
        if os.path.isdir(subfolder_path1) and os.path.isdir(subfolder_path2):
            # List image files in both subfolders
            images1 = sorted([f for f in os.listdir(subfolder_path1) if f.endswith(('.jpg', '.png'))])
            images2 = sorted([f for f in os.listdir(subfolder_path2) if f.endswith(('.jpg', '.png'))])

            # Compare the number of images and remove excess if necessary
            if len(images1) > len(images2):
                # Remove excess images in the first subfolder
                for img in images1[len(images2):]:
                    os.remove(os.path.join(subfolder_path1, img))
                print(f"Removed {len(images1) - len(images2)} excess images from {subfolder_path1}")
            elif len(images2) > len(images1):
                # Remove excess images in the second subfolder
                for img in images2[len(images1):]:
                    os.remove(os.path.join(subfolder_path2, img))
                print(f"Removed {len(images2) - len(images1)} excess images from {subfolder_path2}")

# Specify the paths to your two main folders
folder1 = '/lfs/mercury1/0/willyc/watchdog/watchdog/real_interpolated'
folder2 = '/lfs/mercury1/0/willyc/watchdog/watchdog/real_frames'

remove_excess_frames(folder1, folder2)
