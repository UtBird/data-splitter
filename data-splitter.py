import os
import random
import shutil

# === Ayarlanabilir oranlar ===
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# === Girdi klasörleri ===
image_dir = "model/image"
label_dir = "model/labels"

# === Çıktı klasörleri ===
output_base = "dataset_split"
splits = ['train', 'val', 'test']
for split in splits:
    os.makedirs(os.path.join(output_base, split, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_base, split, 'labels'), exist_ok=True)

# === Veri eşleştirme ===
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
image_files.sort()

random.shuffle(image_files)

total = len(image_files)
train_end = int(train_ratio * total)
val_end = train_end + int(val_ratio * total)

split_files = {
    'train': image_files[:train_end],
    'val': image_files[train_end:val_end],
    'test': image_files[val_end:]
}

# === Dosyaları taşıma ===
for split, files in split_files.items():
    for img_file in files:
        label_file = img_file.rsplit('.', 1)[0] + '.txt'
        
        src_img = os.path.join(image_dir, img_file)
        src_label = os.path.join(label_dir, label_file)

        dst_img = os.path.join(output_base, split, 'images', img_file)
        dst_label = os.path.join(output_base, split, 'labels', label_file)

        shutil.copy2(src_img, dst_img)
        if os.path.exists(src_label):
            shutil.copy2(src_label, dst_label)

print("✅ Veri seti başarıyla ayrıldı!")
