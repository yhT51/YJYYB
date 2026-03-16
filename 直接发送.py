import smtplib
from email.mime.text import MIMEText
import json

# 读取配置
with open(r"C:\Users\Administrator\.agentmail\config.json", "r") as f:
    config = json.load(f)

# 创建邮件
msg = MIMEText("小龙虾测试")
msg["From"] = config["email"]
msg["To"] = "yinhao@jingyunsu.com"
msg["Subject"] = "直接发送测试"

# 发送
server = smtplib.SMTP_SSL("smtp.163.com", 465, timeout=30)
server.login(config["email"], config["password"])
server.sendmail(config["email"], "yinhao@jingyunsu.com", msg.as_string())
server.quit()

print("邮件发送成功")
