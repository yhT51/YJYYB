import os
import sys

print("Python 环境测试")
print("="*50)
print(f"Python version: {sys.version}")
print(f"Current dir: {os.getcwd()}")
print("="*50)

# 测试网络连接
try:
    import socket
    print("\nTest network connection...")
    socket.create_connection(("smtp.163.com", 465), timeout=5)
    print("OK: Can connect to smtp.163.com:465")
except Exception as e:
    print(f"FAIL: Network connection error: {e}")

# 测试文件写入
try:
    test_file = r"D:\XLX\XLXWJ\test_write.txt"
    with open(test_file, "w") as f:
        f.write("test write")
    print("OK: Can write files")
except Exception as e:
    print(f"FAIL: File write error: {e}")

# 测试SMTP
try:
    import smtplib
    import json
    with open(r"C:\Users\Administrator\.agentmail\config.json", "r") as f:
        config = json.load(f)
    print("\nTest SMTP connection...")
    server = smtplib.SMTP_SSL("smtp.163.com", 465, timeout=30)
    server.login(config["email"], config["password"])
    server.quit()
    print("OK: SMTP connection works")
except Exception as e:
    print(f"FAIL: SMTP error: {e}")

print("="*50)
