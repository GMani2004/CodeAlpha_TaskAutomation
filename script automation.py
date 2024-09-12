
import os
import shutil

# Function definition
def organize_files_by_extension(directory):
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Iterate through each file
    for file in files:
        # Get the file extension
        file_extension = file.split('.')[-1]
        # Create a folder name based on the file extension
        folder_name = file_extension.upper() + '_Files'
        folder_path = os.path.join(directory, folder_name)

        # Create the folder if it does not exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move the file into the corresponding folder
        shutil.move(os.path.join(directory, file), os.path.join(folder_path, file))

    print("Files have been organized by extension!")

# Replace this path with your actual directory path
directory_path = r'C:\Users\Jarom Jerwin P\Desktop'  # Using a raw string


# Call the function after its definition
organize_files_by_extension(directory_path)
