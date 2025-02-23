import cv2
import numpy as np
import random
import os

# Gaussian Gürültü
def add_gaussian_noise(image, mean=0, sigma=25):
    noise = np.random.normal(mean, sigma, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image

# Salt & Pepper Gürültüsü
def add_salt_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02):
    noisy_image = np.copy(image)
    total_pixels = image.size
    
    num_salt = int(total_pixels * salt_prob)
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1]] = 255  # Beyaz noktalar
    
    num_pepper = int(total_pixels * pepper_prob)
    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1]] = 0  # Siyah noktalar
    
    return noisy_image

# Poisson Gürültüsü
def add_poisson_noise(image):
    noise = np.random.poisson(image).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image




dataset_path = r"C:\Users\Lenovo\Desktop\colab_ikarus"

# Tüm veri seti için gürültü ekleme işlemi
for folder in ["train", "valid", "test"]:
    src_images = os.path.join(dataset_path, folder, "images")
    dst_images = os.path.join(dataset_path, folder + "_noisy", "images")
    
    for img_file in os.listdir(src_images):
        img_path = os.path.join(src_images, img_file)
        img = cv2.imread(img_path)
        
        if img is not None:
            # Rastgele bir gürültü seç
            noise_type = random.choice(["gaussian", "salt_pepper", "poisson"])
            
            if noise_type == "gaussian":
                noisy_img = add_gaussian_noise(img)
            elif noise_type == "salt_pepper":
                noisy_img = add_salt_pepper_noise(img)
            else:
                noisy_img = add_poisson_noise(img)
            
            # Yeni görüntüyü kaydet
            cv2.imwrite(os.path.join(dst_images, img_file), noisy_img)

print("Tüm görüntülere gürültü başarıyla eklendi!")
