import os
from PIL import Image
import argparse
from tqdm import tqdm

def resample_images(source_folder, output_folder, new_size):

    # 获取所有图像文件
    files = [f for f in os.listdir(source_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 使用 tqdm 显示进度条
    for filename in tqdm(files, desc="重采样进度"):
        img_path = os.path.join(source_folder, filename)
        img = Image.open(img_path)

        # 重采样图像
        img_resampled = img.resize(new_size, Image.LANCZOS)

        # 保存重采样后的图像
        output_path = os.path.join(output_folder, filename)
        img_resampled.save(output_path)

    print("所有图像重采样完成！")

if __name__ == "__main__":
    # 创建解析器
    parser = argparse.ArgumentParser(description="批量重采样文件夹中的图像")
    
    # 添加参数
    parser.add_argument('--source_folder', type=str, required=True, help='源文件夹路径')
    parser.add_argument('--output_folder', type=str, required=True, help='输出文件夹路径')
    parser.add_argument('--width', type=int, required=True, help='重采样宽度')
    parser.add_argument('--height', type=int, required=True, help='重采样高度')

    # 解析参数
    args = parser.parse_args()

    # 调用重采样函数
    resample_images(args.source_folder, args.output_folder, (args.width, args.height))

