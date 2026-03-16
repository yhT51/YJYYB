print("Python 测试")
print("="*50)

try:
    import requests
    print("✓ requests 模块可用")

    import json
    print("✓ json 模块可用")

    # 读取配置
    with open(r"C:\Users\Administrator\.agentmail\config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    print("✓ 配置文件读取成功")
    print(f"  邮箱: {config.get('agentmail_email')}")
    print(f"  API Key: {config.get('agentmail_api_key', '')[:20]}...")

except ImportError as e:
    print(f"✗ 模块导入失败: {e}")
except Exception as e:
    print(f"✗ 错误: {e}")
    import traceback
    traceback.print_exc()

print("="*50)
input("按回车键继续...")
