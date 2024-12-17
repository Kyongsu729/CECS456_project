import os
import random
import shutil

random.seed(42)

data_path = "natural_images/"

# path to destination folders
train_folder= os.path.join(data_path, 'train')
val_folder = os.path.join(data_path, 'val')
test_folder = os.path.join(data_path, 'test')

c_dirs = os.listdir(data_path)
# make folders
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

for c in c_dirs:
    c_path = os.path.join(data_path, c)
    if os.path.isdir(c_path):
        os.makedirs(os.path.join(train_folder,c), exist_ok=True)
        os.makedirs(os.path.join(val_folder,c), exist_ok=True)
        os.makedirs(os.path.join(test_folder,c), exist_ok=True)
        images = [f for f in os.listdir(c_path) if f.endswith(".jpg")]
        random.shuffle(images)
        total_images = len(images)
        train_count = int(0.6 * total_images)
        val_count = int(0.2 * total_images)
        train_images = images[:train_count]
        val_images = images[train_count:train_count+val_count]
        test_images = images[train_count+val_count:]
        
        for img in train_images:
            shutil.copy(os.path.join(c_path, img), os.path.join(train_folder, c, img))
        for img in val_images:
            shutil.copy(os.path.join(c_path, img), os.path.join(val_folder, c, img))
        for img in test_images:
            shutil.copy(os.path.join(c_path, img), os.path.join(test_folder, c, img))