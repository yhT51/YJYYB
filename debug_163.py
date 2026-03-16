"""
在本地 PowerShell 手动运行此脚本查看详细错误：
python D:\XLX\XLXWJ\debug_163.py
"""

import smtplib
from email.mime.text import MIMEText
import json

print("="*50)
print("163邮件发送调试")
print("="*50)

# 读取配置
try:
    with open(r"C:\Users\Administrator\.agentmail\config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    print("\n配置信息:")
    print(f"邮箱: {config['email']}")
    print(f"SMTP服务器: {config['smtp_server']}")
    print(f"端口: {config['smtp_port']}")
    print(f"授权码: {config['password']}")
except Exception as e:
    print(f"✗ 配置文件读取失败: {e}")
    input("按回车退出...")
    exit(1)

# 创建邮件
msg = MIMEText("小龙虾测试")
msg["From"] = config["email"]
msg["To"] = "yinhao@jingyunsu.com"
msg["Subject"] = "20263131350测试"

# 测试SMTP连接
print("\n" + "="*50)
print("步骤1: 测试SMTP连接")
print("="*50)

try:
    print(f"连接 {config['smtp_server']}:{config['smtp_port']}...")
    server = smtplib.SMTP_SSL(config['smtp_server'], config['smtp_port'], timeout=30)
    print("✓ 连接成功")

    # 测试登录
    print("\n" + "="*50)
    print("步骤2: 测试登录")
    print("="*50)
    print(f"使用 {config['email']} 登录...")

    server.login(config['email'], config['password'])
    print("✓ 登录成功")

    # 测试发送
    print("\n" + "="*50)
    print("步骤3: 测试发送")
    print("="*50)
    print(f"发送到: yinhao@jingyunsu.com")

    result = server.sendmail(config['email'], "yinhao@jingyunsu.com", msg.as_string())
    print(f"✓ 发送结果: {result}")

    server.quit()

    print("\n" + "="*50)
    print("邮件发送完成")
    print("="*50)

except smtplib.SMTPAuthenticationError as e:
    print(f"\n✗ 认证失败: {e}")
    print("\n可能的原因:")
    print("1. 163邮箱SMTP服务未开启")
    print("2. 授权码不正确")
    print("3. 授权码已过期")
    print("\n请检查:")
    print("- 登录163邮箱 → 设置 → POP3/SMTP/IMAP")
    print("- 确认SMTP服务已开启")
    print("- 重新生成授权码")

except smtplib.SMTPException as e:
    print(f"\n✗ SMTP错误: {e}")

except Exception as e:
    print(f"\n✗ 发送失败: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*50)
input("按回车键退出...")
