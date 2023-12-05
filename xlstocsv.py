import pandas as pd

# 读取Excel文件
name = 'typhoon'
excel_file_path = name + '.xlsx'
excel_data = pd.ExcelFile(excel_file_path)

# 获取Excel文件中的所有sheet名称
sheet_names = excel_data.sheet_names

# 读取第一个sheet的数据作为基础
merged_df = excel_data.parse(sheet_names[0])

# 合并后续sheet的数据，忽略它们的标记行
for sheet_name in sheet_names[1:]:
    # 读取sheet数据，跳过第一行（标记行）
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name, skiprows=1)
    
    # 合并到主DataFrame
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# 生成CSV文件
merged_csv_file = name + '.csv'
merged_df.to_csv(merged_csv_file, index=False)

print(f"Merged data from all sheets (ignoring subsequent sheet's tags) and saved to {merged_csv_file}.")
