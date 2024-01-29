import os

def rename_files(folder_path, new_folder_path):
    # Get the list of files in the specified folder
    files = os.listdir(folder_path)

    # Filter only PDF files
    pdf_files = [file for file in files if file.endswith('.pdf')]

    # Iterate through the PDF files and rename them
    for i, file in enumerate(pdf_files, start=1):
        # Extract the base filename without extension
        base_filename, extension = os.path.splitext(file)
        # print(base_filename)
        # print(extension)
        if base_filename[-1] == '.':
            new_filename = f"{base_filename[:-1]}-4{extension}"
        else:
            new_filename = f"{base_filename}-3{extension}"
                    
        print(new_filename)
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(new_folder_path, new_filename)

        os.rename(old_path, new_path)

        print(f"Renamed: {file} -> {new_filename}")

folder_path = '11'
new_folder_path = '12'

# Call the function to rename files in the specified folder
rename_files(folder_path, new_folder_path)
