import os
import shutil

def organize_files(directory):
    # Dictionary to map file extensions to folder names
    file_types = {
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Scripts': ['.py', '.sh', '.js'],
        'Others': []  # For files with unknown extensions
    }

    # Create folders if they don't exist
    for folder_name in file_types.keys():
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Determine which folder the file should go into
        moved = False
        for folder_name, extensions in file_types.items():
            if file_extension in extensions:
                destination_folder = os.path.join(directory, folder_name)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Moved {filename} to {folder_name}/")
                moved = True
                break

        # If the file extension is not in the dictionary, move it to 'Others'
        if not moved:
            destination_folder = os.path.join(directory, 'Others')
            shutil.move(file_path, os.path.join(destination_folder, filename))
            print(f"Moved {filename} to Others/")

if __name__ == "__main__":
    # Specify the directory you want to organize
    directory_to_organize = "C:/Users/RsLogik/Desktop/c++/test"

    # Call the function to organize files
    organize_files(directory_to_organize)