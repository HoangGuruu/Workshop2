import os

def list_all_objects(startpath):
    for root, dirs, files in os.walk(startpath):
        for directory in dirs:
            print(os.path.join(root, directory).replace("\\", "/"))  # Thư mục
        for file in files:
            print(os.path.join(root, file).replace("\\", "/"))  # Tệp tin
        for name in os.listdir(root):
            path = os.path.join(root, name)
            if os.path.islink(path):
                print(path.replace("\\", "/"))  # Liên kết tượng trưng

# Thay đổi 'path_to_folder' thành đường dẫn tới thư mục bạn muốn liệt kê
path_to_folder = 'c:/WorkSpace/GitHub/Working/ws/Workshop2/static/WorkShop2/'

list_all_objects(path_to_folder)
