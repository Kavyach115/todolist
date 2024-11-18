import json

class ToDoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description):
        task = {"description": description, "completed": False}
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            return
        for i, task in enumerate(self.tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. [{status}] {task['description']}")

    def update_task(self, index, new_description):
        try:
            self.tasks[index - 1]["description"] = new_description
            self.save_tasks()
        except IndexError:
            print("Invalid task number!")

    def toggle_task_completion(self, index):
        try:
            self.tasks[index - 1]["completed"] = not self.tasks[index - 1]["completed"]
            self.save_tasks()
        except IndexError:
            print("Invalid task number!")

    def delete_task(self, index):
        try:
            self.tasks.pop(index - 1)
            self.save_tasks()
        except IndexError:
            print("Invalid task number!")

    def run(self):
        while True:
            print("\n1. Add Task\n2. List Tasks\n3. Update Task\n4. Toggle Completion\n5. Delete Task\n6. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                desc = input("Enter task description: ").strip()
                self.add_task(desc)
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.list_tasks()
                index = int(input("Enter task number to update: "))
                new_desc = input("Enter new description: ").strip()
                self.update_task(index, new_desc)
            elif choice == "4":
                self.list_tasks()
                index = int(input("Enter task number to toggle completion: "))
                self.toggle_task_completion(index)
            elif choice == "5":
                self.list_tasks()
                index = int(input("Enter task number to delete: "))
                self.delete_task(index)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again!")

if __name__ == "__main__":
    app = ToDoApp()
    app.run()