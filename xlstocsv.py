import pandas as pd

# 读取Excel文件
name = 'earthquake'
excel_file_path = name + '.xlsx'
excel_data = pd.ExcelFile(excel_file_path)

# 获取Excel文件中的所有sheet名称
sheet_names = excel_data.sheet_names

# 初始化一个空的DataFrame用于存储合并后的数据
merged_df = pd.DataFrame()

# 逐个读取sheet并上下拼接到主DataFrame
for sheet_name in sheet_names:
    # 读取sheet数据
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    
    # 上下拼接到主DataFrame
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# 生成CSV文件
merged_csv_file = name + '.csv'
merged_df.to_csv(merged_csv_file, index=False)

print(f"Merged data from all sheets (concatenated vertically) and saved to {merged_csv_file}.")
