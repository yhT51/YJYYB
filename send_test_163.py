import requests
import json

# 读取配置
with open(r"C:\Users\Administrator\.agentmail\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print("="*50)
print("发送邮件到 yhworkbuddytest@163.com")
print("="*50)
print(f"发件人: {config['agentmail_email']}")
print(f"收件人: yhworkbuddytest@163.com")
print(f"内容: 测试你好，我是小龙虾")
print("-"*50)

try:
    print("正在发送...")
    response = requests.post(
        f"https://api.agentmail.to/v0/inboxes/{config['agentmail_email']}/messages",
        headers={
            "Authorization": f"Bearer {config['agentmail_api_key']}",
            "Content-Type": "application/json"
        },
        json={
            "to": "yhworkbuddytest@163.com",
            "subject": "测试",
            "text": "测试你好，我是小龙虾"
        }
    )
    print(f"状态码: {response.status_code}")
    print(f"响应: {response.text}")

    if response.status_code == 200 or response.status_code == 201:
        print("\n✓ 邮件发送成功")
    else:
        print(f"\n✗ 发送失败，状态码: {response.status_code}")

except Exception as e:
    print(f"✗ 错误: {e}")
    import traceback
    traceback.print_exc()

print("="*50)
