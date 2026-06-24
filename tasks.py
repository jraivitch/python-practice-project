import json
import os
import sys

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(description):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "done": False,
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task #{task['id']}: {description}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. Add one with: python tasks.py add \"your task\"")
        return
    print(f"{'ID':<4} {'Status':<10} Description")
    print("-" * 40)
    for task in tasks:
        status = "[done]" if task["done"] else "[ ]"
        print(f"{task['id']:<4} {status:<10} {task['description']}")


def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Marked task #{task_id} as done.")
            return
    print(f"No task found with ID {task_id}.")


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"No task found with ID {task_id}.")
        return
    save_tasks(new_tasks)
    print(f"Deleted task #{task_id}.")


def print_usage():
    print("Usage:")
    print("  python tasks.py add \"task description\"  - Add a new task")
    print("  python tasks.py list                    - List all tasks")
    print("  python tasks.py done <id>               - Mark a task complete")
    print("  python tasks.py delete <id>             - Delete a task")


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task description.")
            print("  Example: python tasks.py add \"Buy groceries\"")
        else:
            add_task(sys.argv[2])

    elif command == "list":
        list_tasks()

    elif command == "done":
        if len(sys.argv) < 3:
            print("Please provide a task ID.")
            print("  Example: python tasks.py done 1")
        else:
            complete_task(int(sys.argv[2]))

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Please provide a task ID.")
            print("  Example: python tasks.py delete 1")
        else:
            delete_task(int(sys.argv[2]))

    else:
        print(f"Unknown command: {command}")
        print_usage()


if __name__ == "__main__":
    main()
