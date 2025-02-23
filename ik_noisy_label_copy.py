import shutil
import os

dataset_path = r"C:\Users\Lenovo\Desktop\colab_ikarus"

for folder in ["train", "valid", "test"]:
    src_labels = os.path.join(dataset_path, folder, "labels")
    dst_labels = os.path.join(dataset_path, folder + "_noisy", "labels")
    
    for label_file in os.listdir(src_labels):
        shutil.copy(os.path.join(src_labels, label_file), os.path.join(dst_labels, label_file))

print("Etiket dosyaları başarıyla kopyalandı!")
