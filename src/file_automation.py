import os
import shutil
import logging

# Set up logging
log_directory = 'D:/FileAutomationProject/logs'

def show_menu():
    print("File Management Menu:")
    print("1. List Files")
    print("2. Create Directory")
    print("3. Move File")
    print("4. Copy File")
    print("5. Delete File")
    print("6. Exit")

def list_files():
    path = input("Enter the directory path: ")
    try:
        files = os.listdir(path)
        if not files:
            print("The directory is empty.")
        else:
            for file_name in files:
                print(file_name)
    except FileNotFoundError:
        print("Directory not found. Please check the path.")
    except PermissionError:
        print("Permission denied.")

def create_directory():
    path = input("Enter the new directory path: ")
    try:
        os.mkdir(path)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print("Directory already exists.")
    except PermissionError:
        print("Permission denied.")
    except OSError as e:
        print(f"Error creating directory: {e}")

def move_file():
    source = input("Enter the source file path: ")
    destination = input("Enter the destination directory path: ")
    if not os.path.exists(source):
        print("Source file does not exist.")
        return
    if not os.path.isdir(destination):
        print("Destination directory does not exist.")
        return
    # Proceed with the move if inputs are valid
    try:
        shutil.move(source, destination)
        print(f"File moved from '{source}' to '{destination}'")
    except Exception as e:
        print(f"Error: {e}")

def copy_file():
    source = input("Enter the source file or directory path: ")
    destination = input("Enter the destination directory path: ")
    try:
        if os.path.isdir(source):
            shutil.copytree(source, os.path.join(destination, os.path.basename(source)))
            print(f"Directory copied from '{source}' to '{destination}'")
        else:
            shutil.copy(source, destination)
            print(f"File copied from '{source}' to '{destination}'")
    except FileNotFoundError:
        print("Source file or destination directory not found.")
    except PermissionError:
        print("Permission denied.")
    except OSError as e:
        print(f"Error copying file: {e}")
    
def delete_file():
    path = input("Enter the file or folder path to delete: ")
    
    try:
        # Check if it's a file
        if os.path.isfile(path):
            os.remove(path)
            print(f"File '{path}' deleted.")
        # Check if it's a directory (folder), empty or not
        elif os.path.isdir(path):
            # Use shutil.rmtree to delete the folder and all its contents
            shutil.rmtree(path)
            print(f"Folder '{path}' and all its contents deleted.")
        else:
            print("Invalid path. Please enter a valid file or folder path.")
    except FileNotFoundError:
        print("File or folder not found.")
    except PermissionError:
        print("Permission denied.")
    except OSError as e:
        print(f"Error deleting file or folder: {e}")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            list_files()
        elif choice == '2':
            create_directory()
        elif choice == '3':
            move_file()
        elif choice == '4':
            copy_file()
        elif choice == '5':
            delete_file()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print(f"You chose option {choice}. Functionality coming soon!")

if __name__ == "__main__":
    main()
