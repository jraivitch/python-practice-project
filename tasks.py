import json
import os
import re
import sys
from datetime import datetime

TASKS_FILE = "tasks.json"


def parse_due_date(date_str):
    cleaned = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str.strip())
    for fmt in ["%B %d", "%b %d", "%m/%d", "%B %d %Y", "%b %d %Y", "%m/%d/%Y"]:
        try:
            parsed = datetime.strptime(cleaned, fmt)
            if parsed.year == 1900:
                today = datetime.today()
                parsed = parsed.replace(year=today.year)
                if parsed.date() < today.date():
                    parsed = parsed.replace(year=today.year + 1)
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
VALID_PRIORITIES = set(PRIORITY_ORDER)


def add_task(description, priority="medium", due_date=None):
    if priority not in VALID_PRIORITIES:
        print(f"Invalid priority '{priority}'. Choose from: low, medium, high")
        return
    if due_date is not None:
        parsed = parse_due_date(due_date)
        if parsed is None:
            print(f"Could not parse due date '{due_date}'. Try something like 'June 26th' or '6/26'.")
            return
        due_date = parsed
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "done": False,
        "priority": priority,
        "due_date": due_date,
    }
    tasks.append(task)
    save_tasks(tasks)
    due_str = f" due {due_date}" if due_date else ""
    print(f"Added task #{task['id']}: {description} [{priority}]{due_str}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. Add one with: python tasks.py add \"your task\"")
        return
    sorted_tasks = sorted(tasks, key=lambda t: PRIORITY_ORDER.get(t.get("priority", "medium"), 1))
    print(f"{'ID':<4} {'Status':<10} {'Priority':<10} {'Due':<12} Description")
    print("-" * 66)
    for task in sorted_tasks:
        status = "[done]" if task["done"] else "[ ]"
        priority = task.get("priority", "medium")
        due = task.get("due_date") or ""
        print(f"{task['id']:<4} {status:<10} {priority:<10} {due:<12} {task['description']}")


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
    print("  python tasks.py add \"task description\" [--priority low|medium|high] [--due \"June 26th\"]  - Add a new task")
    print("  python tasks.py list                                                                      - List all tasks")
    print("  python tasks.py done <id>                                                                 - Mark a task complete")
    print("  python tasks.py delete <id>                                                               - Delete a task")


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
            priority = "medium"
            due_date = None
            args = sys.argv[3:]
            if "--priority" in args:
                idx = args.index("--priority")
                if idx + 1 < len(args):
                    priority = args[idx + 1]
            if "--due" in args:
                idx = args.index("--due")
                if idx + 1 < len(args):
                    due_date = args[idx + 1]
            add_task(sys.argv[2], priority, due_date)

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
