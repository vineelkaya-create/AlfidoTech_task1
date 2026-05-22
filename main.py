# Import required modules
import os
import shutil

# Function to read a text file
def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        print("\nFile Content:")
        print(content)

    except FileNotFoundError:
        print("Error: File not found")

    except Exception as e:
        print("Something went wrong:", e)


# Function to write data into file
def write_file(filename, text):
    try:
        with open(filename, "a") as file:
            file.write(text)

        print("\nData written successfully")

    except Exception as e:
        print("Error while writing:", e)


# Function to rename file
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"\nFile renamed from {old_name} to {new_name}")

    except FileNotFoundError:
        print("Rename Error: File not found")

    except Exception as e:
        print("Rename Error:", e)


# Function to move file
def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"\nFile moved to {destination}")

    except FileNotFoundError:
        print("Move Error: File not found")

    except Exception as e:
        print("Move Error:", e)


# Function to delete file
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"\n{filename} deleted successfully")

    except FileNotFoundError:
        print("Delete Error: File not found")

    except Exception as e:
        print("Delete Error:", e)


# ---------------- MAIN PROGRAM ---------------- #

print("===== Python File Handling & Automation =====")

# Step 1: Write into file
write_file("sample.txt", "\nWelcome to Python Internship Task")

# Step 2: Read file
read_file("sample.txt")

# Step 3: Rename file
rename_file("sample.txt", "updated_sample.txt")

# Step 4: Create folder if not exists
folder_name = "files"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("\nFolder created:", folder_name)

# Step 5: Move file into folder
move_file("updated_sample.txt", "files/updated_sample.txt")

# Step 6: Delete file example
delete_file("test.csv")

print("\nAutomation Task Completed")