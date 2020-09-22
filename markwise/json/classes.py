"""
markwise.JSON
JSON wrapper for Python
"""

# Imports
import json

class JSONManager:
    """Manages JSON files"""
    def __init__(self, filename=None):
        self.filename = filename
        
        if self.filename != None:
            self.load_json(self.filename)
        else:
            self.raw_json = {}

    def load_json(self, filename=None):
        """Load a specified JSON file"""
        if filename == None:
            filename = self.filename
            
        with open(filename, "r+") as f:
            self.raw_json = json.load(f)
    
    def create_key(self, name, value=None):
        """Create a key for the JSON file to later save. If you want to append a dictionary, use createKeysFromDict() instead"""
        self.raw_json.update({name : value})

    def create_keys_from_dict(self, dictionary):
        """Appends a Python dictionary to the JSON file"""
        self.raw_json.update(dictionary)
        
    def update_key(self, name, value):
        """Update a value of a certain JSON key"""
        self.raw_json[name] = value
        
    def remove_key(self, name):
        """Remove a key from the JSON file"""
        self.raw_json.pop(name)
        
    def save_json(self, filename=None, format_json=True):
        """Save a JSON file to the specified location"""
        if filename == None:
            filename = self.filename
        
        with open(filename, "w+") as f:
            if format_json:
                json.dump(self.raw_json, f, indent = 4)
            else:
                json.dump(self.raw_json, f)
