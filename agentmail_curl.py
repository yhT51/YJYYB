import requests

# 读取配置
import json
with open(r"C:\Users\Administrator\.agentmail\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# 创建日志
log = open(r"D:\XLX\XLXWJ\curl_log.txt", "w")

try:
    log.write("使用 AgentMail API 发送邮件\n")
    log.write("="*50 + "\n")

    # 获取邮箱列表
    log.write("获取邮箱列表...\n")
    response = requests.get(
        "https://api.agentmail.to/v0/inboxes",
        headers={"Authorization": f"Bearer {config['agentmail_api_key']}"}
    )
    log.write(f"状态码: {response.status_code}\n")
    log.write(f"响应: {response.text}\n")

    if response.status_code == 200:
        inboxes = response.json()
        if inboxes.get("inboxes"):
            inbox_id = inboxes["inboxes"][0]["id"]
            log.write(f"使用邮箱: {inbox_id}\n")

            # 发送邮件
            log.write("开始发送邮件...\n")
            send_response = requests.post(
                f"https://api.agentmail.to/v0/inboxes/{inbox_id}/messages",
                headers={
                    "Authorization": f"Bearer {config['agentmail_api_key']}",
                    "Content-Type": "application/json"
                },
                json={
                    "to": "yinhao@jingyunsu.com",
                    "subject": "问候",
                    "text": "你好，我是你的小龙虾"
                }
            )
            log.write(f"发送状态码: {send_response.status_code}\n")
            log.write(f"发送响应: {send_response.text}\n")
        else:
            log.write("没有找到邮箱，需要先创建\n")

    log.write("="*50 + "\n")

except Exception as e:
    log.write(f"错误: {e}\n")
    import traceback
    log.write(traceback.format_exc())
finally:
    log.close()
