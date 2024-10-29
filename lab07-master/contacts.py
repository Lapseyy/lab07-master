import json
# import os

class Contacts:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}
    
    def add_contact(self, id, first_name, last_name):
        
        
        try:
            if id in self.data:
                return "error"
            self.data[id] = [first_name, last_name]
            # self.data[id] = dict(sorted(self.data.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
        
            self.data = dict(sorted(self.data.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
        except IndexError as e:
            print(f"Error: Incorrect contact format encountered - {e}")
            return "error: contact format issue"
        
        self.write_to_file()
        
        return {id: [first_name, last_name]}
    
    def modify_contact(self, id, first_name, last_name):
        if id not in self.data:
            return "error"
        self.data[id] =  [first_name, last_name]
        self.data = dict(sorted(self.data.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
        self.write_to_file()
        return {id: [first_name, last_name]}
    
    
    def delete_contact(self, id):
        if id not in self.data:
            return "error"
        remove = self.data.pop(id)
        self.write_to_file()
        return {id: remove}
    
    # Fucntion to write to the file. 
    def write_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent= 4)