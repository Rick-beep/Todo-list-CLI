import json

class List():
    def __init__(self, data):
        self.__id = data["id"]
        self.content = data["content"]
        
    def __str__(self):
        return f"Id: {self.get_id}, Content: {self.content}"

    
    def add_content(self, inputed_content):
        self.content = inputed_content
    
    @property
    def get_id(self):
        return self.__id


class Todolist():
    def __init__(self):
        self.all_list = self.load_json()
        self.main()
    
    def main(self):
        while True:
            self.command_line_interface()
            
    def load_json(self):
        output = []
        with open("save-file.json") as file:
            data = json.load(file)
            
        for task in data["tasks"]:
            output.append(List(task))
        
        for i in output:
            print(i)
            
            
    def command_line_interface(self):
        def print_commands():
            print("add")
            print("update")
            print("delete")
            print("mark")
            print("list")
        
        def execute_command(cmd_line: str):
            cmd = cmd_line.split(" ")    
            match cmd[0]:
                case "help":
                    print_commands()
                case "add":
                    print("sssssssssss")
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