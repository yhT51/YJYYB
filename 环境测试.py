import os
import sys

print("Python 环境测试")
print("="*50)
print(f"Python 版本: {sys.version}")
print(f"当前目录: {os.getcwd()}")
print(f"环境变量 PATH: {os.environ.get('PATH', '')[:200]}")
print("="*50)

# 测试网络连接
try:
    import socket
    print("\n测试网络连接...")
    socket.create_connection(("smtp.163.com", 465), timeout=5)
    print("✓ 可以连接 smtp.163.com:465")
except Exception as e:
    print(f"✗ 网络连接失败: {e}")

# 测试文件写入
try:
    test_file = r"D:\XLX\XLXWJ\test_write.txt"
    with open(test_file, "w") as f:
        f.write("测试写入")
    print("✓ 可以写入文件")
except Exception as e:
    print(f"✗ 文件写入失败: {e}")

print("="*50)
