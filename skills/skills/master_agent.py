from skills.data_agent import handle as data_handle
from skills.content_agent import handle as content_handle

def master_agent(task: str):
    task_lower = task.lower()

    if any(word in task_lower for word in ["data", "analysis", "csv", "excel"]):
        return data_handle(task)

    elif any(word in task_lower for word in ["post", "content", "caption", "write"]):
        return content_handle(task)

    else:
        return f"[GENERAL AGENT] I understand the task but no specific skill matched: {task}"

if __name__ == "__main__":
    while True:
        user_task = input("Tell me what to do (type exit to quit): ")
        if user_task.lower() == "exit":
            break
        print(master_agent(user_task))
