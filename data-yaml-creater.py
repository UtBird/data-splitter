import yaml

def create_yolov8_data_yaml(base_path="model", names_file="model/obj.names", output_file="model/data.yaml"):
    # Sınıf isimlerini oku
    with open(names_file, 'r') as f:
        class_names = [line.strip() for line in f if line.strip()]

    data_yaml = {
        'train': f'{base_path}/train/images',
        'val': f'{base_path}/val/images',
        'test': f'{base_path}/test/images',
        'nc': len(class_names),
        'names': class_names
    }

    with open(output_file, 'w') as f:
        yaml.dump(data_yaml, f, default_flow_style=False)

    print(f"✅ YOLOv8 için 'data.yaml' oluşturuldu:\n-> {output_file}")

# === KULLANIM ===
create_yolov8_data_yaml()
