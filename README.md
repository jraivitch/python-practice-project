# Python Task Tracker

A beginner-friendly command-line task tracker built with Python. Use this project to practice Python basics and GitHub workflows.

## What it does

- Add tasks
- List all tasks with their status
- Mark tasks as complete
- Delete tasks
- Saves tasks to a `tasks.json` file so they persist between runs

## Requirements

- Python 3 (no extra packages needed)

## How to run

Open a terminal in this project folder, then use any of these commands:

```bash
# Add a task
python tasks.py add "Buy groceries"

# List all tasks
python tasks.py list

# Mark task #1 as done
python tasks.py done 1

# Delete task #1
python tasks.py delete 1
```

## Example session

```
$ python tasks.py add "Buy groceries"
Added task #1: Buy groceries

$ python tasks.py add "Walk the dog"
Added task #2: Walk the dog

$ python tasks.py list
ID   Status     Description
----------------------------------------
1    [ ]        Buy groceries
2    [ ]        Walk the dog

$ python tasks.py done 1
Marked task #1 as done.

$ python tasks.py list
ID   Status     Description
----------------------------------------
1    [done]     Buy groceries
2    [ ]        Walk the dog

$ python tasks.py delete 2
Deleted task #2.
```

## File overview

| File | Purpose |
|------|---------|
| `tasks.py` | Main program — all the logic lives here |
| `tasks.json` | Where your tasks are saved (created automatically) |

## GitHub practice ideas

- **Fork** this repo and make your own changes
- **Create a branch** and add a new feature (e.g., due dates, priorities)
- **Open a pull request** to practice the PR workflow
- **Write an issue** describing a bug or feature you'd like to add
