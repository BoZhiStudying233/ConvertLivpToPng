import os
import zipfile


def convert_livp_to_jpg(root_path):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith('.livp'):
                # 构建完整的文件路径，包括子文件夹
                full_path = os.path.join(root, file)
                # 将 livp 文件重命名为 zip 文件
                zip_path = os.path.splitext(full_path)[0] + '.zip'
                os.rename(full_path, zip_path)
        unzip_files(root_path)

def unzip_files(root_path):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.zip'):
                try:
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(root)
                    print(f"Unzipped {file_path} successfully.")
                except Exception as e:
                    print(f"Failed to unzip {file_path}: {e}")
            elif file.endswith('.rar'):
                try:
                    with rarfile.RarFile(file_path, 'r') as rar_ref:
                        rar_ref.extractall(root)
                    print(f"Unzipped {file_path} successfully.")
                except Exception as e:
                    print(f"Failed to unzip {file_path}: {e}")

def delete_rest_files(root_path):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith('.mov') or file.endswith('.livp') or file.endswith('.zip') or file.endswith('.rar'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted {file_path} successfully.")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")


def rename_heic_to_png(root_path):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith('.heic'):
                # 构建完整的文件路径，包括子文件夹
                full_path = os.path.join(root, file)
                # 生成新的文件路径，将后缀改为.png
                new_path = os.path.splitext(full_path)[0] + '.png'
                try:
                    # 重命名文件
                    os.rename(full_path, new_path)
                    print(f"Renamed {full_path} to {new_path} successfully.")
                except Exception as e:
                    print(f"Failed to rename {full_path} to {new_path}: {e}")


if __name__ == "__main__":
    root_path = r'C:\Users\BoZhi\Desktop\照片'
    convert_livp_to_jpg(root_path)
    delete_rest_files(root_path)
    rename_heic_to_png(root_path)
