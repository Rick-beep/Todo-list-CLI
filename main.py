import json
from random import randint
class Task():
    def __init__(self, data):
        self.__id = data["id"]
        self.task = data["task"]
        self.status = data["status"]        
        
    def __str__(self):
        return f'id: "{self.get_id}", task: "{self.task}", status: "{self.status}"'

    def retrive_data(self):
        return {"id": self.get_id, "task": self.task, "status": self.status}
    @property
    def get_id(self):   
        return self.__id
class Todolist():
    def __init__(self):
        self.all_tasks = self.load_json()
        self.main()
    
    def main(self):
        while True:
            self.command_line_interface()
            self.save_to_json()
                        
    def load_json(self):
        output = []
        try:
            with open("save-file.json") as file:
                data = json.load(file)
            for task in data["tasks"]:
                output.append(Task(task))
        
        except:
            pass
            
        return output
    
    def save_to_json(self):
        tasks_data = []
        for task in self.all_tasks:
            tasks_data.append(task.retrive_data())
            
        save_file = {"tasks": tasks_data}
        with open("save-file.json", "w") as file:
            json.dump(save_file, file)
            
    def find_task(self, task_id):
        for task in self.all_tasks:
            if task_id == task.retrive_data["id"]:
                return task
            else:
                return None
        
    def generate_id(self): 
        def generator(): #Generate id string 5 digits
            task_id = str(randint(1, 999))
            while len(task_id) < 3:
                task_id = "0" + task_id
            return task_id
        
        while True:
            task_id = generator()
            for task in self.all_tasks:
                task_data = task.retrive_data()
                if task_data["id"] == task_id:
                    continue
            break
            
        return task_id
            
    def command_line_interface(self):
        for i in self.all_tasks: #Print semua task
            print(i)
            
        def print_commands():
            print("add; add new task")
            print("ls; List all command")
            print("rm; Remove task")
            print("mk; Mark done task")
            print("sv; Saves the task")
        
        def add_task():
            task = input("Task: ")
            task_id = self.generate_id()
            
            data = {"id": task_id, "task": task, "status": False}
            self.all_tasks.append(Task(data))
        
        def delete_task(): # !!! BUAT FUNGSI UNTUK MENGHAPUS TASK !!!
            task_id = int(input("Input the task ID: "))
            print(self.all_tasks[task_id])
            self.all_tasks.pop(task_id)          

        def execute_command(cmd_line: str):
            match cmd_line:
                case "help":
                    print_commands()
                case "add":
                    add_task()
                case "sv":
                    pass
                case "rm":
                    delete_task()
                case "mk":
                    pass
                case "ls":
                    pass
            
        cmd_line = input()
        execute_command(cmd_line)
    
if __name__ == "__main__":
    Todolist()

"""
    Add, Update, and Delete tasks

    Mark a task as in progress or done

    List all tasks

    List all tasks that are done

    List all tasks that are not done

    List all tasks that are in progress
"""