def create_and_write_file():
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Line 1: Hello, world!\n")
            file.write("Line 2: Python is fun.\n")
            file.write("Line 3: 1234567890\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def read_and_display_file():
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File content after initial write:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Line 4: Appending text.\n")
            file.write("Line 5: More Python.\n")
            file.write("Line 6: End of file.\n")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()

if __name__ == "__main__":
    main()
