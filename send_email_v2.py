import smtplib
from email.mime.text import MIMEText
import json

# 读取配置
with open(r"C:\Users\Administrator\.agentmail\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# 创建邮件
msg = MIMEText("你好，我是你的小龙虾")
msg["From"] = config["email"]
msg["To"] = "yinhao@jingyunsu.com"
msg["Subject"] = "问候"

try:
    server = smtplib.SMTP_SSL(config["smtp_server"], config["smtp_port"], timeout=30)
    server.login(config["email"], config["password"])
    result = server.sendmail(config["email"], "yinhao@jingyunsu.com", msg.as_string())
    server.quit()
    print("发送成功", result)
except Exception as e:
    print("发送失败", str(e))
    import traceback
    traceback.print_exc()
