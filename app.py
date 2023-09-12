import os
from PIL import Image

def one_or_two():
    while True:
        selection = input()
        if selection in ['1', '2']:
            break
        else:
            print("Invalid input. Please enter 1 or 2.")
    return selection

def remove_within_folder():
        
        files = []
        to_delete = []

        while True:
            my_folder = input("Enter path to folder:\n")
            if os.path.isdir(my_folder):
                break
            else:
                print("Invalid input. Enter a valid folder path.")
            
        for filename in os.listdir(my_folder):
            files.append(Image.open(my_folder + "\\" + filename))

        seen = []
        for img in files:
            for i in seen:
                if img == i:
                    to_delete.append(i.filename)
            else:
                seen.append(img)

        for entry in to_delete:
            os.remove(entry)
            print("Removed" + entry)


def remove_between_folders():
    print("Enter paths to two different folders of photos:")
    while True:
        folder1 = input("Enter first folder:\n")
        if os.path.isdir(folder1):
            break
        else:
            print("Invalid input. Enter a valid folder path.")
        
    while True:
        folder2 = input("Enter second folder:\n")
        if os.path.isdir(folder2):
            if folder2 != folder1:
                break
            else:
                print("Choose a unique folder.")
        else:
            print("Invalid input. Enter a valid folder path.")
    print("Delete duplicates from\n1: " + folder1 + "\n2: " + folder2)
    selection = one_or_two()

    f1_files = []
    f2_files = []

    to_delete = []

    for filename in os.listdir(folder1):
        f1_files.append(filename)

    for filename in os.listdir(folder2):
        f2_files.append(filename)

    for fname1 in f1_files:
        img1 = Image.open(folder1 + "\\" + fname1)
        for fname2 in f2_files:
            img2 = Image.open(folder2 + "\\" + fname2)
            if img1 == img2:
                if selection == 1:
                    to_delete.append(folder1 + "\\" + fname1)
                else:
                    to_delete.append(folder2 + "\\" + fname2)

    for entry in to_delete:
        os.remove(entry)
        print("Removed" + entry)

def main():
    print("Remove \n1: Duplicates within a folder \n2: Duplicates between two folders")
    selection = one_or_two()
    if selection == "1":
        remove_within_folder()
    elif selection == "2":
        remove_between_folders()
    

if __name__ == "__main__":
    main()