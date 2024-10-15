# src/file_automation.py

def show_menu():
    print("File Management Menu:")
    print("1. List Files")
    print("2. Create Directory")
    print("3. Move File")
    print("4. Copy File")
    print("5. Delete File")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '6':
            print("Exiting...")
            break
        else:
            print(f"You chose option {choice}. Functionality coming soon!")

if __name__ == "__main__":
    main()
