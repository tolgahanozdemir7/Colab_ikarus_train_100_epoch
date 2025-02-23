import random
import os

dataset_path = r"C:\Users\Lenovo\Desktop\colab_ikarus"

data_yaml_path = os.path.join(dataset_path, "data_noisy.yaml")

with open(data_yaml_path, "w") as f:
    f.write(f"train: {dataset_path}/train_noisy/images\n")
    f.write(f"val: {dataset_path}/valid_noisy/images\n")
    f.write(f"test: {dataset_path}/test_noisy/images\n")
    f.write("nc: 1\n")  # Sınıf sayısı (Gereksinime göre değiştir)
    f.write("names: ['object']\n")  # Sınıf isimleri (Değiştir)

print("Yeni data.yaml dosyasi oluşturuldu: data_noisy.yaml")

