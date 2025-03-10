'''
Description: 
Autor: name
Date: 2025-02-20 15:35:52
LastEditors: name
LastEditTime: 2025-02-20 15:58:06
'''
import subprocess
import json
 
def send_request_to_ollama(prompt):
    # 构造Ollama的请求命令
    command = [
        "ollama", "send", "deepseek-r1:1.5b",  # 确保模型名称正确，这里仅为示例
        "-i", "-",  # 表示从标准输入读取输入
        "-o", "-"   # 表示将输出发送到标准输出
    ]
    # 使用subprocess运行命令，并通过管道传递prompt和接收输出
    result = subprocess.run(command, input=prompt, capture_output=True, text=True)
    # result = subprocess.run(command, input=prompt.encode('utf-8'), capture_output=True, text=True)
    return result.stdout
 
# 示例使用
prompt = "你好，DeepSeek！请告诉我一些关于人工智能的信息。"
response = send_request_to_ollama(prompt)
print(response)
