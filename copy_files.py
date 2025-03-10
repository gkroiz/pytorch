import shutil
import os

src_dir = "/workspace/pytorch/torch/distributed/checkpoint"
dst_dir = "/usr/local/lib/python3.10/dist-packages/torch/distributed/checkpoint"

# Ensure the destination directory exists
os.makedirs(dst_dir, exist_ok=True)

# Copy all files from src_dir to dst_dir
for root, _, files in os.walk(src_dir):
    rel_path = os.path.relpath(root, src_dir)
    dest_path = os.path.join(dst_dir, rel_path)
    os.makedirs(dest_path, exist_ok=True)

    for file in files:
        shutil.copy2(os.path.join(root, file), os.path.join(dest_path, file))

print("Files copied successfully.")

