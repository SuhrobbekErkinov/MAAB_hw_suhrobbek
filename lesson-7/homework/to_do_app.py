import csv
import json
from abc import ABC, abstractmethod

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["task_id"],
            data["title"],
            data["description"],
            data.get("due_date"),
            data["status"],
        )

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


# Storage Strategy Interface
class StorageStrategy(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass


# CSV Storage Implementation
class CSVStorage(StorageStrategy):
    FILE_NAME = "tasks.csv"

    def save(self, tasks):
        with open(self.FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load(self):
        tasks = []
        try:
            with open(self.FILE_NAME, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(Task(row["Task ID"], row["Title"], row["Description"], row["Due Date"], row["Status"]))
        except FileNotFoundError:
            pass
        return tasks


# JSON Storage Implementation
class JSONStorage(StorageStrategy):
    FILE_NAME = "tasks.json"

    def save(self, tasks):
        with open(self.FILE_NAME, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

    def load(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                return [Task.from_dict(task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []


# To-Do Manager Class
class ToDoManager:
    def __init__(self, storage_strategy):
        self.storage_strategy = storage_strategy
        self.tasks = self.storage_strategy.load()

    def add_task(self, task_id, title, description, due_date=None, status="Pending"):
        task = Task(task_id, title, description, due_date, status)
        self.tasks.append(task)
        self.storage_strategy.save(self.tasks)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                self.storage_strategy.save(self.tasks)
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.storage_strategy.save(self.tasks)
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print(f"No tasks found with status '{status}'.")
        else:
            for task in filtered_tasks:
                print(task)


# User Interaction
def main():
    # Choose storage format
    print("Select storage format: 1. CSV  2. JSON")
    choice = input("Enter choice (1/2): ")

    storage = CSVStorage() if choice == "1" else JSONStorage()
    manager = ToDoManager(storage)

    while True:
        print("\nTo-Do Application")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
            status = input("Enter Status (Pending/In Progress/Completed): ")
            manager.add_task(task_id, title, description, due_date, status)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title (leave blank to keep unchanged): ") or None
            description = input("Enter new Description (leave blank to keep unchanged): ") or None
            due_date = input("Enter new Due Date (YYYY-MM-DD, optional): ") or None
            status = input("Enter new Status (Pending/In Progress/Completed): ") or None
            manager.update_task(task_id, title, description, due_date, status)

        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            manager.delete_task(task_id)

        elif choice == "5":
            status = input("Enter Status to filter (Pending/In Progress/Completed): ")
            manager.filter_tasks(status)

        elif choice == "6":
            print("Exiting To-Do Application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
