import requests
import json

# 读取配置
with open(r"C:\Users\Administrator\.agentmail\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

try:
    print("正在发送邮件到 yhworkbuddytest@163.com...")

    response = requests.post(
        f"https://api.agentmail.to/v0/inboxes/{config['agentmail_email']}/messages",
        headers={
            "Authorization": f"Bearer {config['agentmail_api_key']}",
            "Content-Type": "application/json"
        },
        json={
            "to": "yhworkbuddytest@163.com",
            "subject": "测试",
            "text": "小龙虾测试"
        }
    )

    if response.status_code == 200 or response.status_code == 201:
        print("✓ 邮件发送成功")
    else:
        print(f"✗ 发送失败: {response.status_code} - {response.text}")

except Exception as e:
    print(f"✗ 错误: {e}")
