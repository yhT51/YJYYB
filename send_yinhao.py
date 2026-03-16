import smtplib
from email.mime.text import MIMEText
import json

# 读取配置
with open(r"C:\Users\Administrator\.agentmail\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print("使用163邮箱发送邮件到 yinhao@jingyunsu.com")
print("="*50)
print(f"发件人: {config['email']}")
print(f"收件人: yinhao@jingyunsu.com")
print(f"内容: 小龙虾测试")
print("-"*50)

try:
    # 创建邮件
    msg = MIMEText("小龙虾测试")
    msg["From"] = config["email"]
    msg["To"] = "yinhao@jingyunsu.com"
    msg["Subject"] = "测试"

    # 连接SMTP服务器
    print("连接到 smtp.163.com:465...")
    server = smtplib.SMTP_SSL("smtp.163.com", 465, timeout=30)
    print("连接成功")

    # 登录
    print(f"登录 {config['email']}...")
    server.login(config["email"], config["password"])
    print("登录成功")

    # 发送
    print("发送邮件...")
    result = server.sendmail(config["email"], "yinhao@jingyunsu.com", msg.as_string())
    print(f"发送结果: {result}")

    server.quit()
    print("\n✓ 邮件发送成功")

except smtplib.SMTPAuthenticationError as e:
    print(f"\n✗ 认证失败: {e}")
    print("请检查163邮箱SMTP服务和授权码")

except Exception as e:
    print(f"\n✗ 发送失败: {e}")
    import traceback
    traceback.print_exc()

print("="*50)
