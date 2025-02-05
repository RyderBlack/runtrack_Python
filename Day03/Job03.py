class Task:
    def __init__(self, task_title, task_description):
        self.task_title = task_title
        self.task_description = task_description
        self.task_status = "To Do"

    def __str__(self):
        return f"{self.task_title} ({self.task_status}): {self.task_description}"

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def mark_as_completed(self, task):
        task.task_status = "Completed"

    def display_list(self):
        for task in self.tasks:
            print(task)

    def filter_list(self, status):
        filtered_tasks = [task for task in self.tasks if task.task_status == status]
        return filtered_tasks




task_list = TaskList()

task1 = Task("Buy groceries", "Milk, eggs, bread")
task2 = Task("Clean the house", "Vacuum, mop, dust")
task3 = Task("Work on project", "Finish coding the website")

task_list.add_task(task1)
task_list.add_task(task2)
task_list.add_task(task3)

print("All tasks:")
task_list.display_list()

task_list.mark_as_completed(task2)

# print("\nTasks to be done:")
# to_do_tasks = task_list.filter_list("To Do")
# for task in to_do_tasks:
#     print(task)

task_list.remove_task(task3)

print("\nRemaining tasks:")
task_list.display_list()