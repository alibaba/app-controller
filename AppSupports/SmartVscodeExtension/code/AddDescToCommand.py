import sys
import json
import time
import requests

from Common.ProgressTracker import ProgressTracker


def get_response(query, model="gpt-4-turbo-2024-04-09"):
    url = "https://api.mit-spider.alibaba-inc.com/chatgpt/api/ask"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjIyNTE4NiIsInBhc3N3b3JkIjoiMjI1MTg2IiwiZXhwIjoyMDA2OTMzNTY1fQ.wHKJ7AdJ22yPLD_-1UHhXek4b7uQ0Bxhj_kJjjK0lRM"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": query}],
        "response_format": {"type": "json_object"},
        "n": 1,
        "temperature": 0.0
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()


def get_desc(input_prompt, stop=None) -> str:
    response = get_response(input_prompt)
    print(response)
    # this is structure for ali-gpt not work for chatgpt
    data = response['data']['response']['choices'][0]['message']['content'].strip()
    return json.loads(data)["desc"]


# files = ["vscode", "workbench", "search", "editor", "notebook"]
files = ["workbench", "search", "editor", "notebook"]

prompt = """
This is the command of vscode. Please fill in the missing desc of the command. Answer should be in JSON format.
{
"commandId": "original command",
"desc": "description"
}.

An example:
{
  "commandId": "workbench.action.files.openLocalFileFolder",
  "desc": "Opens a native OS dialog to select a local file or folder to open in VS Code."
}.

My command is {command}.
"""

if __name__ == "__main__":
    for file in files:
        file = "Core/MetaData/Commands/system/" + file + ".json"
        with open(file, "r") as f:
            print(f"Processing {file}")
            commands = json.loads(f.read())
            for i in range(len(commands)):
                tracker = ProgressTracker(len(commands))
                command = commands[i]
                while True:
                    try:
                        if command["desc"] == "":
                            command["desc"] = get_desc(prompt.replace("{command}", command["commandId"]))
                            print(command)
                        tracker.update(1)
                        break  # 成功执行后跳出内嵌循环
                    except Exception as e:
                        print(f"遇到异常，重试中... 错误: {e}")
                        continue
        with open(file, "w") as f:
            f.write(json.dumps(commands, indent=4))
