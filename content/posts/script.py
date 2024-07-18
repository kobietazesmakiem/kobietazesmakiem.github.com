import os

def rename_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(f'File: {file}')
            if "-scaled" in file:
                print(f'File: {file}')
                # Create the new filename by removing '-sliced'
                new_filename = file.replace("-scaled", "")
                # Construct the full file path
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, new_filename)

                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {old_file_path} -> {new_file_path}')

# Example usage
rename_files_in_directory(".")