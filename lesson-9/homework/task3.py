import json
import csv


def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    print("ID | Task Name | Completed | Priority")
    print("-" * 40)
    for task in tasks:
        print(f"{task['id']} | {task['task']} | {task['completed']} | {task['priority']}")


def calculate_task_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks else 0

    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")


def convert_json_to_csv(json_filename="tasks.json", csv_filename="tasks.csv"):
    tasks = load_tasks(json_filename)
    if not tasks:
        print("No tasks found to convert.")
        return

    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print(f"Tasks saved to {csv_filename}")

if __name__ == "__main__":
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_task_stats(tasks)
    convert_json_to_csv()
