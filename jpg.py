import os

def change_image_extensions_to_jpg(folder_path):
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"The folder '{folder_path}' does not exist.")
            return
        
        # Loop through all files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Skip directories
            if os.path.isdir(file_path):
                continue
            
            # Get file name and extension
            name, ext = os.path.splitext(filename)
            
            # Skip files that already have .jpg extension
            if ext.lower() == ".jpg":
                continue
            
            # Rename the file with .jpg extension
            new_filename = f"{name}.jpg"
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")
        
        print("All image extensions have been changed to .jpg.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
folder_path = "history"  # Replace with the path to your folder
change_image_extensions_to_jpg(folder_path)
