"""
请在本地 PowerShell 手动运行此脚本查看详细错误信息：
python D:\XLX\XLXWJ\manual_test.py
"""

import requests
import json

# 读取配置
print("读取配置...")
with open(r"C:\Users\Administrator\.agentmail\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print(f"API Key: {config['agentmail_api_key']}")
print(f"邮箱: {config['agentmail_email']}")
print("\n" + "="*50)

# 1. 测试 API Key
print("\n1. 测试 API Key...")
headers = {"Authorization": f"Bearer {config['agentmail_api_key']}"}
response = requests.get("https://api.agentmail.to/v0/inboxes", headers=headers)
print(f"状态码: {response.status_code}")
print(f"响应: {response.text}")

if response.status_code != 200:
    print("\n✗ API Key 无效或已过期")
    input("按回车退出...")
    exit(1)

# 2. 检查邮箱是否存在
print("\n2. 检查邮箱...")
response = requests.get(f"https://api.agentmail.to/v0/inboxes/{config['agentmail_email']}", headers=headers)
print(f"状态码: {response.status_code}")
print(f"响应: {response.text}")

if response.status_code != 200:
    print("\n✗ 邮箱不存在或未激活")
    print("请登录 https://console.agentmail.to 确认邮箱状态")
    input("按回车退出...")
    exit(1)

# 3. 尝试发送
print("\n3. 尝试发送邮件...")
send_data = {
    "to": "yhworkbuddytest@163.com",
    "subject": "测试",
    "text": "小龙虾测试"
}
print(f"发送数据: {send_data}")

response = requests.post(
    f"https://api.agentmail.to/v0/inboxes/{config['agentmail_email']}/messages",
    headers=headers,
    json=send_data
)

print(f"\n状态码: {response.status_code}")
print(f"响应: {response.text}")

if response.status_code in [200, 201]:
    print("\n✓ 邮件发送成功")
else:
    print(f"\n✗ 发送失败")
    if response.status_code == 401:
        print("错误: API Key 无效")
    elif response.status_code == 404:
        print("错误: 邮箱不存在")
    elif response.status_code == 422:
        print("错误: 请求参数无效")
    elif response.status_code == 429:
        print("错误: 发送频率限制")

print("\n" + "="*50)
input("按回车退出...")
