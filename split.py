import os
import numpy as np
import shutil

# # Creating Train / Val / Test folders (One time use)
root_dir = 'Pictures/van/'

os.makedirs(root_dir +'train')
os.makedirs(root_dir +'val')
os.makedirs(root_dir +'test')

# Creating partitions of the data after shuffeling
src = root_dir + 'all/' # Folder to copy images from

allFileNames = os.listdir(src)
np.random.shuffle(allFileNames)
train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                                          [int(len(allFileNames)*0.7), int(len(allFileNames)*0.85)])


train_FileNames = [src+ name for name in train_FileNames.tolist()]
val_FileNames = [src + name for name in val_FileNames.tolist()]
test_FileNames = [src + name for name in test_FileNames.tolist()]

print('Total images: ', len(allFileNames))
print('Training: ', len(train_FileNames))
print('Validation: ', len(val_FileNames))
print('Testing: ', len(test_FileNames))

# Copy-pasting images
for name in train_FileNames:
    shutil.copy(name, root_dir + "train")

for name in val_FileNames:
    shutil.copy(name, root_dir + "val")

for name in test_FileNames:
    shutil.copy(name, root_dir + "test")
