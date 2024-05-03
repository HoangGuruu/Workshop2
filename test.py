import os

def list_all_objects(startpath):
    for root, dirs, files in os.walk(startpath):
        for directory in dirs:
            relative_path = os.path.relpath(os.path.join(root, directory), startpath).replace("\\", "/")
            print("![](../../WorkShop2/{}?featherlight=false&width=90pc)".format(relative_path))  # Thư mục
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), startpath).replace("\\", "/")
            print("![](../../WorkShop2/{}?featherlight=false&width=90pc)".format(relative_path))  # Tệp tin
        for name in os.listdir(root):
            path = os.path.join(root, name)
            if os.path.islink(path):
                relative_path = os.path.relpath(path, startpath).replace("\\", "/")
                print("![](../../WorkShop2/{}?featherlight=false&width=90pc)".format(relative_path))  # Liên kết tượng trưng

# Thay đổi 'path_to_folder' thành đường dẫn tới thư mục bạn muốn liệt kê
path_to_folder = 'c:/WorkSpace/GitHub/Working/ws/Workshop2/static/WorkShop2/'

list_all_objects(path_to_folder)
