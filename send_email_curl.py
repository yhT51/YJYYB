import smtplib
from email.mime.text import MIMEText
import json

# 读取配置
with open(r"C:\Users\Administrator\.agentmail\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# 创建日志
log = open(r"D:\XLX\XLXWJ\email_debug.txt", "w")

try:
    log.write("配置信息:\n")
    log.write(f"SMTP: {config['smtp_server']}:{config['smtp_port']}\n")
    log.write(f"邮箱: {config['email']}\n")
    log.write(f"授权码: {config['password']}\n\n")

    msg = MIMEText("你好，我是你的小龙虾")
    msg["From"] = config["email"]
    msg["To"] = "yinhao@jingyunsu.com"
    msg["Subject"] = "问候"

    log.write("开始连接...\n")
    server = smtplib.SMTP_SSL(config["smtp_server"], config["smtp_port"])
    log.write("连接成功\n")

    log.write("开始登录...\n")
    server.login(config["email"], config["password"])
    log.write("登录成功\n")

    log.write("开始发送...\n")
    result = server.sendmail(config["email"], "yinhao@jingyunsu.com", msg.as_string())
    log.write(f"发送结果: {result}\n")

    server.quit()
    log.write("邮件已发送\n")

except Exception as e:
    log.write(f"错误: {e}\n")
    import traceback
    log.write(traceback.format_exc())
finally:
    log.close()
