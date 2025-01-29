import os

def create_file(filename, content=""):
    """Creates a new file with optional content."""
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}' created successfully.")

def read_file(filename):
    """Reads the content of a file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        print(f"\nContents of '{filename}':\n{content}")
    else:
        print(f"Error: File '{filename}' does not exist.")

def append_to_file(filename, content):
    """Appends content to an existing file."""
    if os.path.exists(filename):
        with open(filename, 'a') as file:
            file.write("\n" + content)
        print(f"Content appended to '{filename}'.")
    else:
        print(f"Error: File '{filename}' does not exist.")

def delete_file(filename):
    """Deletes a file."""
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    else:
        print(f"Error: File '{filename}' does not exist.")

def list_files():
    """Lists all text files in the current directory."""
    files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.txt')]
    if files:
        print("\nAvailable text files:")
        for file in files:
            print(f"- {file}")
    else:
        print("No text files found.")

def main():
    """Main function to handle user input."""
    while True:
        print("\nFile Management System")
        print("1. Create File")
        print("2. Read File")
        print("3. Append to File")
        print("4. Delete File")
        print("5. List Files")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            filename = input("Enter file name (with .txt extension): ")
            content = input("Enter file content (leave empty for a blank file): ")
            create_file(filename, content)

        elif choice == '2':
            filename = input("Enter file name to read: ")
            read_file(filename)

        elif choice == '3':
            filename = input("Enter file name to append to: ")
            content = input("Enter content to append: ")
            append_to_file(filename, content)

        elif choice == '4':
            filename = input("Enter file name to delete: ")
            delete_file(filename)

        elif choice == '5':
            list_files()

        elif choice == '6':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()