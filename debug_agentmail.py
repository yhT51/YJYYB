import requests
import json

# 读取配置
with open(r"C:\Users\Administrator\.agentmail\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# 写入日志文件
log = open(r"D:\XLX\XLXWJ\debug_log.txt", "w", encoding="utf-8")

try:
    log.write("="*50 + "\n")
    log.write("AgentMail API 调试\n")
    log.write("="*50 + "\n")
    log.write(f"API Key: {config['agentmail_api_key']}\n")
    log.write(f"邮箱: {config['agentmail_email']}\n\n")

    # 1. 测试 API 连接
    log.write("1. 测试 API 连接...\n")
    headers = {"Authorization": f"Bearer {config['agentmail_api_key']}"}

    # 获取邮箱列表
    log.write("获取邮箱列表...\n")
    response = requests.get("https://api.agentmail.to/v0/inboxes", headers=headers)
    log.write(f"状态码: {response.status_code}\n")
    log.write(f"响应: {response.text}\n\n")

    # 2. 检查指定邮箱是否存在
    log.write("2. 检查邮箱是否存在...\n")
    response = requests.get(f"https://api.agentmail.to/v0/inboxes/{config['agentmail_email']}", headers=headers)
    log.write(f"状态码: {response.status_code}\n")
    log.write(f"响应: {response.text}\n\n")

    # 3. 列出邮箱消息
    log.write("3. 列出邮箱消息...\n")
    response = requests.get(f"https://api.agentmail.to/v0/inboxes/{config['agentmail_email']}/messages", headers=headers)
    log.write(f"状态码: {response.status_code}\n")
    log.write(f"响应: {response.text}\n\n")

    # 4. 尝试发送邮件
    log.write("4. 尝试发送邮件...\n")
    send_data = {
        "to": "yhworkbuddytest@163.com",
        "subject": "测试",
        "text": "测试你好，我是小龙虾"
    }
    response = requests.post(
        f"https://api.agentmail.to/v0/inboxes/{config['agentmail_email']}/messages",
        headers=headers,
        json=send_data
    )
    log.write(f"状态码: {response.status_code}\n")
    log.write(f"响应: {response.text}\n\n")

    log.write("="*50 + "\n")
    log.write("调试完成\n")
    log.write("="*50 + "\n")

except Exception as e:
    log.write(f"错误: {e}\n")
    import traceback
    log.write(traceback.format_exc())
finally:
    log.close()
