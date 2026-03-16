"""
将鄱阳工单数据转换为和革命伤残军人休养院运维报告相同的格式
"""

import pandas as pd

# 读取两个文件
poyang_file = r"D:\XLX\XLXWJ\鄱阳工单数据_1773391976677.xlsx"
soldier_file = r"D:\XLX\XLXWJ\革命伤残军人休养院云净血透系统运维报告.docx"

print("读取鄱阳工单数据...")
try:
    df = pd.read_excel(poyang_file)
    print(f"成功读取，共 {len(df)} 行数据")
    print("\n数据列名:")
    print(df.columns.tolist())
    print("\n前5行数据:")
    print(df.head())
except Exception as e:
    print(f"读取失败: {e}")
    input("按回车退出...")
    exit(1)

print("\n读取革命伤残军人休养院运维报告...")
print("注意: .docx 文件需要转换为 .docx 格式才能直接分析")
print("请确保该文件已经是 .docx 格式")
