import json

class Task():
    def __init__(self, data):
        self.__id = data["id"]
        self.content = data["content"]
        
    def __str__(self):
        return f"id: {self.get_id}, content: {self.content}"

    def retrive_data(self):
        return {"id": self.get_id, "content": self.content}
        
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
            self.update_tasks()
                     
    def load_json(self):
        output = []
        with open("save-file.json") as file:
            data = json.load(file)
            
        for task in data["tasks"]:
            output.append(Task(task))
    
        return output
    
    def save_to_json(self):
        tasks_data = []
        for task in self.all_tasks:
            tasks_data.append(task.retrive_data())
            
        save_file = {"tasks": tasks_data}
        
        with open("save-file.json", "w") as file:
            json.dump(save_file, file)
              
    def update_tasks(self):
        pass
            
    def command_line_interface(self):
        for i in self.all_tasks:
            print(i)
            
        def print_commands():
            print("add")
            print("update")
            print("delete")
            print("mark")
            print("list")
        
        def add_task(content):
            def generate_id():
                return len(self.all_tasks)
            
            task_id = generate_id()
            task_content = content
            data = {"id": task_id, "content": task_content}

            self.all_tasks.append(Task(data))
        
        def execute_command(cmd_line: str):
            cmd = cmd_line.split(" ")    
            match cmd[0]:
                case "help":
                    print_commands()
                case "add":
                    if cmd[1][0] == "'" and cmd[1][-1] == "'" or cmd[1][0] == '"' and cmd[1][-1] == '"':   
                        k = cmd[1][1:-1]
                        add_task(k)
                    else:
                        print("wrong input")
                    
                case "update":
                    pass
                case "delete":
                    pass
                case "mark":
                    pass
                case "list":
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