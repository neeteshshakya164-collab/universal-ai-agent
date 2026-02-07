from skills.data_agent import handle as data_handle
from skills.content_agent import handle as content_handle

def master_agent(task: str):
    task_lower = task.lower()

    if "data" in task_lower or "csv" in task_lower:
        file_path = input("Enter CSV file path: ")
        return data_handle(task, file_path)

    elif any(word in task_lower for word in ["post", "content", "caption", "write"]):
        return content_handle(task)

    else:
        return f"[GENERAL AGENT] Task received: {task}"

if __name__ == "__main__":
    while True:
        user_task = input("\nTell me what to do (type exit to quit): ")
        if user_task.lower() == "exit":
            break
        print(master_agent(user_task))
