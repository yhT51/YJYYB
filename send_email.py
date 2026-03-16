import smtplib
from email.mime.text import MIMEText
import json
import time

# 读取配置
with open(r"C:\Users\Administrator\.agentmail\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# 创建日志文件
log_file = open(r"D:\XLX\XLXWJ\email_log.txt", "w", encoding="utf-8")

try:
    log_file.write("="*50 + "\n")
    log_file.write("开始发送邮件\n")
    log_file.write("="*50 + "\n")
    log_file.write(f"SMTP服务器: {config['smtp_server']}\n")
    log_file.write(f"端口: {config['smtp_port']}\n")
    log_file.write(f"邮箱: {config['email']}\n")
    log_file.write(f"授权码: {config['password'][:4]}****\n")
    log_file.write("="*50 + "\n")

    # 创建邮件
    msg = MIMEText("你好，我是你的小龙虾")
    msg["From"] = config["email"]
    msg["To"] = "yinhao@jingyunsu.com"
    msg["Subject"] = "问候"

    log_file.write("正在连接SMTP服务器...\n")
    log_file.flush()

    server = smtplib.SMTP_SSL(config["smtp_server"], config["smtp_port"], timeout=30)
    log_file.write("✓ 连接成功\n")
    log_file.flush()

    # 启用调试输出
    server.set_debuglevel(2)

    log_file.write("正在登录...\n")
    log_file.flush()

    server.login(config["email"], config["password"])
    log_file.write("✓ 登录成功\n")
    log_file.flush()

    log_file.write("正在发送邮件...\n")
    log_file.write(f"收件人: yinhao@jingyunsu.com\n")
    log_file.flush()

    result = server.sendmail(config["email"], "yinhao@jingyunsu.com", msg.as_string())
    log_file.write(f"✓ 发送结果: {result}\n")
    log_file.flush()

    server.quit()
    log_file.write("="*50 + "\n")
    log_file.write("邮件发送完成！\n")
    log_file.write("="*50 + "\n")

except smtplib.SMTPAuthenticationError as e:
    log_file.write(f"✗ 认证失败: {e}\n")
    log_file.write("提示: 请检查163邮箱SMTP服务和授权码\n")
    log_file.flush()

except smtplib.SMTPException as e:
    log_file.write(f"✗ SMTP错误: {e}\n")
    log_file.flush()

except Exception as e:
    log_file.write(f"✗ 发送失败: {e}\n")
    import traceback
    log_file.write(traceback.format_exc())
    log_file.flush()

finally:
    log_file.close()
