import os
from shutil import copyfile

# Set source and destination root paths
root = 'E:/MAES/Foto\'s/'
dest_root = 'E:/MAES/Inzending/'

# Ignore some folders
folders = [folder for folder in os.listdir(root) if os.path.isdir(root + folder)]

for folder in folders:
    # Copy the folder over to the destination root folder, if it doesnt exist yet
    if not os.path.exists(dest_root + folder):
        os.mkdir(dest_root + folder)

    # List file in the currently checked folder
    files = [dest_root + folder + '/' + x for x in os.listdir(root + folder) if x.endswith('.jpg')]

    # Loop over all files in the currently checked folder
    for dest_file in files:
        # Create source path from the destination path
        src = dest_file.replace(dest_root, root)
        # Copy file
        copyfile(src, dest_file)

        print(src, '-->', dest_file)
