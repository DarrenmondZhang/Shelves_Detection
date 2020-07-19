from data_prep.dataset import Dataset


date = "Classification"
# 数据路径
dataset_path = f"wine_data/{date}"
# 训练集路径
train_dataset_path = f"{dataset_path}/train"
# 验证集路径
val_dataset_path = f"{dataset_path}/val"

# 划分数据集（首次执行）
# 训练和验证集比例
train_ratio = 0.9
data_loader = Dataset(dataset_path, train_ratio=train_ratio) 