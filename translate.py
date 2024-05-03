

from googletrans import Translator
import os
import re

def translate_md_file(input_file, output_file):
    translator = Translator()
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    translated_lines = []
    
    # Giữ nguyên 7 dòng đầu
    for i in range(7):
        translated_lines.append(lines[i])
        
    # Dịch nội dung từ dòng 8 đến dòng trước dòng cuối
    for line in lines[7:-1]:
        if line.strip() and not is_image_link(line):  # Kiểm tra xem dòng có chứa nội dung không và không phải là đường dẫn hình ảnh
            translated_line = translator.translate(line, src='en', dest='vi').text
            translated_lines.append(translated_line + '\n')  # Thêm ký tự xuống dòng
        else:
            translated_lines.append(line)  # Giữ nguyên dòng nếu là đường dẫn hình ảnh hoặc dòng trống
    
    # Giữ nguyên dòng cuối
    translated_lines.append(lines[-1])
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in translated_lines:
            f.write(line)

def is_image_link(line):
    """
    Kiểm tra xem dòng có chứa đường dẫn hình ảnh không.
    """
    return bool(re.search(r'!\[.*\]\(.*\)', line))

# Sử dụng hàm
input_path = 'C:/WorkSpace/GitHub/Working/ws/Workshop2/content/1-Intro-prepare/1.1-intro/_index.md'
output_path = 'C:/WorkSpace/GitHub/Working/ws/Workshop2/content/1-Intro-prepare/1.1-intro/_index_output.md'
translate_md_file(input_path, output_path)
