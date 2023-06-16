import os
import random
import shutil

# 设置训练集和验证集的比例
train_ratio = 0.8
val_ratio = 0.2

# 遍历当前文件夹下的所有文件夹
for foldername in os.listdir("."):
    if os.path.isdir(foldername):
        if foldername != "val_set" and foldername != "training_set":
        # 创建训练集和验证集文件夹
            train_foldername = os.path.join("training_set", foldername)
            val_foldername = os.path.join("val_set", foldername)
            os.makedirs(train_foldername, exist_ok=True)
            os.makedirs(val_foldername, exist_ok=True)
            images = []
            # 遍历每个文件夹中的图片
            for file in os.listdir(foldername):
                images.append(file)
            
            random.shuffle(images)
            train_count = int(len(images) * train_ratio)
            train_images = images[:train_count]
            val_images = images[train_count:]

            # 移动训练集图片
            for i in train_images:
                src = os.path.join(foldername, i)
                dst = os.path.join(train_foldername, i)
                shutil.copyfile(src, dst)
            
            # 移动验证集图片
            for i in val_images:
                src = os.path.join(foldername, i)
                dst = os.path.join(val_foldername, i)
                shutil.copyfile(src, dst)