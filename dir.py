import os

def remove_whitespace_in_filenames(directory):
    # Lấy danh sách tất cả các tập tin trong thư mục
    files = os.listdir(directory)
    # Lặp qua từng tập tin
    for file_name in files:
        # Xây dựng đường dẫn đầy đủ của tập tin
        file_path = os.path.join(directory, file_name)
        # Kiểm tra xem file có phải là file hay không (không phải thư mục)
        if os.path.isfile(file_path):
            # Loại bỏ khoảng trắng từ tên tập tin
            new_file_name = file_name.replace(" ", "")
            # Xây dựng đường dẫn mới với tên tập tin đã được loại bỏ khoảng trắng
            new_file_path = os.path.join(directory, new_file_name)
            # Đổi tên tập tin thành tên mới
            os.rename(file_path, new_file_path)
            print(f"Đã loại bỏ khoảng trắng từ: {file_path} thành {new_file_path}")

# Thay đổi 'path_to_folder' thành đường dẫn tới thư mục bạn muốn kiểm tra và loại bỏ khoảng trắng
path_to_folder = 'c:/WorkSpace/GitHub/Working/ws/Workshop2/static/WorkShop2/08.clear/'
remove_whitespace_in_filenames(path_to_folder)
