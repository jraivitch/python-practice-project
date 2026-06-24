# Python Task Tracker

A beginner-friendly command-line task tracker built with Python. Use this project to practice Python basics and GitHub workflows.

## What it does

- Add tasks with optional priority (`low`, `medium`, `high`)
- List all tasks sorted by priority (high first)
- Mark tasks as complete
- Delete tasks
- Saves tasks to a `tasks.json` file so they persist between runs

## Requirements

- Python 3 (no extra packages needed)

## How to run

Open a terminal in this project folder, then use any of these commands:

```bash
# Add a task (default priority: medium)
python tasks.py add "Buy groceries"

# Add a task with a priority
python tasks.py add "Fix production bug" --priority high
python tasks.py add "Read docs" --priority low

# List all tasks (sorted by priority)
python tasks.py list

# Mark task #1 as done
python tasks.py done 1

# Delete task #1
python tasks.py delete 1
```

## Example session

```
$ python tasks.py add "Buy groceries"
Added task #1: Buy groceries [medium]

$ python tasks.py add "Fix production bug" --priority high
Added task #2: Fix production bug [high]

$ python tasks.py add "Read docs" --priority low
Added task #3: Read docs [low]

$ python tasks.py list
ID   Status     Priority   Description
----------------------------------------------------
2    [ ]        high       Fix production bug
1    [ ]        medium     Buy groceries
3    [ ]        low        Read docs

$ python tasks.py done 2
Marked task #2 as done.

$ python tasks.py list
ID   Status     Priority   Description
----------------------------------------------------
2    [done]     high       Fix production bug
1    [ ]        medium     Buy groceries
3    [ ]        low        Read docs

$ python tasks.py delete 3
Deleted task #3.
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
