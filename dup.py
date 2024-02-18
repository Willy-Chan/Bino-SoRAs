import os
import shutil
import sys

def count_files(folder):
    # Count the number of files in the folder
    count = sum(1 for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file)))
    return count

def is_original(filename):
    # Check if a filename corresponds to an original file
    return not filename.endswith("dup")

def duplicate_files(source_folder):
    # Ensure source folder exists
    if not os.path.exists(source_folder):
        print(f"Error: Folder '{source_folder}' does not exist.")
        return

    # Continue duplicating files until the count reaches exactly 2100
    while count_files(source_folder) < 2100:
        # Iterate over files in the source folder
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)

            # Check if the path is a file and if it's an original file
            if os.path.isfile(source_path) and is_original(filename):
                # Construct the destination path with "dup" appended to the filename
                destination_path = os.path.join(source_folder, filename[:-4] + "dup" + filename[-4:])
                
                # Duplicate the file
                shutil.copy(source_path, destination_path)
                #print(f"Duplicated: {filename} to {destination_path}")

                # Break the loop if the count reaches 2100
                #if count_files(source_folder) == 2100:
                 #   break

if __name__ == "__main__":
    # Check if folder argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        duplicate_files(folder_path)
        print(str(count_files(folder_path)) + " files now in " + str(folder_path))