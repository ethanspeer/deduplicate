import os
from PIL import Image

print("Enter paths to two different folders of photos:")
folder1 = input("Enter first folder:")
folder2 = input("Enter second folder:")
while True:
    selection = input("Would you like to remove from the first or second folder, select 1 or 2:")
    if selection in ['1', '2']:
        break
    else:
        print("Invalid input. Please enter 1 or 2.")


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
                to_delete.append(folder1 + "\\" + fname1)

for entry in to_delete:
    os.remove(entry)
    print("Removed" + entry)