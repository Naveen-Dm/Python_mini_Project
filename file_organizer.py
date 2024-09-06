import os
import shutil
import mimetypes
import tkinter as tk
from tkinter import filedialog

# By this Function user can select his directory through a GUI dialog
def get_input_directory():
    try:
        root = tk.Tk()
        root.withdraw()
        input_directory = filedialog.askdirectory(title="Select Input Directory")
        return input_directory
    except Exception as e:
        print(f"Error while selecting input directory: {e}")
        return None

def get_output_directory():
    try:
        root = tk.Tk()
        root.withdraw()
        output_directory = filedialog.askdirectory(title="Select Output Directory")
        return output_directory
    except Exception as e:
        print(f"Error while selecting output directory: {e}")
        return None

# By this Function i am segregating the  files based on their types by using MIME type module 
def segregate_files(directory_path, output_directory):
    try:
        
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

    
        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)

               
                mime_type, encoding = mimetypes.guess_type(file_path)

                # Here i am Creating a directory for the file type in the output directory
                type_directory = os.path.join(output_directory, mime_type)
                if not os.path.exists(type_directory):
                    os.makedirs(type_directory)

                # Here Checking if the file already exists in the destination directory
                destination_path = os.path.join(type_directory, file_name)
                if os.path.exists(destination_path):
                    print(f"File '{file_name}' already exists in '{type_directory}'")
                else:
                    # if the file is not existing iam  Move the file to the corresponding directory
                    shutil.move(file_path, destination_path)
                    print(f"successful organization: {file_name}")

        # Here i am Print the hierarchy destination directory after successful organization
        print("\nHierarchy of Destination Directory:")
        for root, dirs, files in os.walk(output_directory):
            level = root.replace(output_directory, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for file_name in files:
                print('{}{}'.format(subindent, file_name))

    except Exception as e:
        print(f"Error during file segregation: {e}")


try:
    input_directory = get_input_directory()
    output_directory = get_output_directory()

    # Here validating the paths 
    if input_directory and output_directory:
        segregate_files(input_directory, output_directory)
    else:
        print("Error: Invalid input or output directory.")

except PermissionError as pe:
    print(f"Permission error: {pe}")
except Exception as e:
    print(f"Unexpected error: {e}")