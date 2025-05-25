## 📂 Dataset Preparation Tools for YOLOv8

This repository contains two helper Python scripts designed to streamline dataset preparation for YOLOv8 object detection projects.

### 🧩 Contents

* `data-splitter.py`: Splits images and labels into training, validation, and test folders based on specified ratios.
* `data-yaml-creater.py`: Automatically generates a `data.yaml` file compatible with YOLOv8.

---

### 📁 Folder Structure

The expected input folder structure is as follows:

```
model/
├── image/          # All image files (.jpg, .png, etc.)
├── labels/         # Corresponding YOLO-format .txt label files
├── obj.names       # Class list (one class name per line)
```

---

### 🚀 Usage

#### 1. Split the Dataset

```bash
python data-splitter.py
```

This script splits the contents of `model/image/` and `model/labels/` into:

* 70% for training,
* 20% for validation,
* 10% for testing

The split is stored under `dataset_split/`:

```
dataset_split/
├── train/
│   ├── images/
│   └── labels/
├── val/
│   ├── images/
│   └── labels/
├── test/
│   ├── images/
│   └── labels/
```

#### 2. Create the `data.yaml` File

```bash
python data-yaml-creater.py
```

This script reads class names from `model/obj.names` and generates a `data.yaml` file like this:

```yaml
train: model/train/images
val: model/val/images
test: model/test/images
nc: 3
names: ['class1', 'class2', 'class3']
```

> 📌 Note: This `data.yaml` file can be used directly in YOLOv8 training commands.

---

### 📦 Requirements

* Python 3.6+
* `pyyaml` (required for `data-yaml-creater.py`)

Install with:

```bash
pip install pyyaml
```
