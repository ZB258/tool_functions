import os
import shutil
import argparse

def main(source_folder, output_folder_images, output_folder_labels):
    # 创建输出文件夹
    os.makedirs(output_folder_images, exist_ok=True)
    os.makedirs(output_folder_labels, exist_ok=True)

    # 遍历源文件夹
    for filename in os.listdir(source_folder):
        if filename.endswith('.jpg'):
            # 处理图像文件
            img_source_path = os.path.join(source_folder, filename)
            img_output_path = os.path.join(output_folder_images, filename)
            shutil.copy(img_source_path, img_output_path)
            
            # 处理对应的 YOLO 标签文件
            label_filename = filename.replace('.jpg', '.txt')  # 假设标签文件以相同的名称命名
            label_source_path = os.path.join(source_folder, label_filename)
            
            if os.path.exists(label_source_path):
                label_output_path = os.path.join(output_folder_labels, label_filename)
                shutil.copy(label_source_path, label_output_path)

    print("文件分割完成！")

if __name__ == "__main__":
    # 创建解析器
    parser = argparse.ArgumentParser(description="分割数据集为图像和标签")
    
    # 添加参数
    parser.add_argument('--source_folder', type=str, required=True, help='源文件夹路径')
    parser.add_argument('--output_images', type=str, required=True, help='输出图像文件夹路径')
    parser.add_argument('--output_labels', type=str, required=True, help='输出标签文件夹路径')

    # 解析参数
    args = parser.parse_args()

    # 调用主函数
    main(args.source_folder, args.output_images, args.output_labels)

