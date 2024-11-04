import os
import shutil
import random
import argparse

def split_dataset(source_folder, train_folder, val_folder, test_folder, train_ratio, val_ratio,test_ratio):
    
    assert abs((train_ratio + val_ratio + test_ratio) - 1.0) < 1e-6, "训练集、验证集和测试集的比例之和必须为1.0！"
    
    # 创建输出文件夹
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # 获取所有文件
    files = [f for f in os.listdir(source_folder) if f.endswith(('.jpg', '.png'))]


    # 打乱文件顺序
    random.shuffle(files)

    # 计算每个数据集的数量
    total_files = len(files)
    train_count = int(total_files * train_ratio)
    val_count = int(total_files * val_ratio)

    # 分割文件
    train_files = files[:train_count]
    val_files = files[train_count:train_count + val_count]
    test_files = files[train_count + val_count:]

    # 复制文件到相应的文件夹
    for f in train_files:
        #####################################################################################################################
        f_txt=f.split('.')[0]+'.txt'
        shutil.copy(os.path.join(source_folder, f), os.path.join(train_folder, f))
        shutil.copy(os.path.join(source_folder, f_txt), os.path.join(train_folder, f_txt))########################################

    for f in val_files:
        #####################################################################################################################
        f_txt=f.split('.')[0]+'.txt'
        shutil.copy(os.path.join(source_folder, f), os.path.join(val_folder, f))
        shutil.copy(os.path.join(source_folder, f_txt), os.path.join(val_folder, f_txt))########################################

    for f in test_files:
        #####################################################################################################################
        f_txt=f.split('.')[0]+'.txt'
        shutil.copy(os.path.join(source_folder, f), os.path.join(test_folder, f))
        shutil.copy(os.path.join(source_folder, f_txt), os.path.join(test_folder, f_txt))########################################

    print("数据集分割完成！")

if __name__ == "__main__":
    # 创建解析器
    parser = argparse.ArgumentParser(description="分割数据集为训练集、验证集和测试集")
    
    # 添加参数
    parser.add_argument('--source_folder', type=str, required=True, help='源文件夹路径')
    parser.add_argument('--train_folder', type=str, required=True, help='训练集文件夹路径')
    parser.add_argument('--val_folder', type=str, required=True, help='验证集文件夹路径')
    parser.add_argument('--test_folder', type=str, required=True, help='测试集文件夹路径')
    parser.add_argument('--train_ratio', type=float, default=0.7, help='训练集比例（默认为0.7）')
    parser.add_argument('--val_ratio', type=float, default=0.2, help='验证集比例（默认为0.2）')
    parser.add_argument('--test_ratio', type=float, default=0.1, help='测试集比例（默认为0.1）')

    # 解析参数
    args = parser.parse_args()

    # 调用分割函数
    split_dataset(args.source_folder, args.train_folder, args.val_folder, args.test_folder, args.train_ratio, args.val_ratio,args.test_ratio)

