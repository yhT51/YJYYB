from agentmail import AgentMail

# 读取配置
import json
with open(r"C:\Users\Administrator\.agentmail\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

client = AgentMail(api_key=config["agentmail_api_key"])

# 创建日志
log = open(r"D:\XLX\XLXWJ\agentmail_log.txt", "w")

try:
    log.write("使用 AgentMail 发送邮件\n")
    log.write("="*50 + "\n")

    # 列出邮箱
    log.write("列出邮箱列表...\n")
    inboxes = client.inboxes.list()
    log.write(f"邮箱数量: {len(inboxes.inboxes)}\n")

    if inboxes.inboxes:
        inbox_id = inboxes.inboxes[0].id
        log.write(f"使用邮箱: {inbox_id}\n")

        # 发送邮件
        log.write("开始发送...\n")
        result = client.inboxes.messages.send(
            inbox_id=inbox_id,
            to="yinhao@jingyunsu.com",
            subject="问候",
            text="你好，我是你的小龙虾"
        )
        log.write(f"发送成功: {result}\n")
    else:
        log.write("没有找到邮箱，需要先创建\n")

    log.write("="*50 + "\n")

except Exception as e:
    log.write(f"错误: {e}\n")
    import traceback
    log.write(traceback.format_exc())
finally:
    log.close()
