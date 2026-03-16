import requests
import json

# 读取配置
with open(r"C:\Users\Administrator\.agentmail\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# 直接打印结果，不写文件
print("="*50)
print("AgentMail 发送测试")
print("="*50)
print(f"API Key: {config['agentmail_api_key'][:20]}...")
print(f"邮箱: {config['agentmail_email']}")
print("-"*50)

try:
    # 发送邮件
    print("正在发送...")
    response = requests.post(
        f"https://api.agentmail.to/v0/inboxes/{config['agentmail_email']}/messages",
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
    print(f"状态码: {response.status_code}")
    print(f"响应: {response.text}")

    if response.status_code == 200 or response.status_code == 201:
        print("\n邮件发送成功！")
    else:
        print(f"\n发送失败，状态码: {response.status_code}")

except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()

print("="*50)
