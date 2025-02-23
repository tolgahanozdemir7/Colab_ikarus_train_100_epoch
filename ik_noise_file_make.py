import os 
dataset_path = r"C:\Users\Lenovo\Desktop\colab_ikarus"

for folder in ["train_noisy","valid_noisy","test_noisy"]:
    os.makedirs(os.path.join(dataset_path, folder, "images"), exist_ok=True)
    os.makedirs(os.path.join(dataset_path, folder, "labels"), exist_ok=True)

print("gurultu dataset klasorleri succesfully!")