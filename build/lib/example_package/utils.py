from typing import Optional

class Printer:
    
    @staticmethod
    def say_hello(name: Optional[str] = None):
        if name is None:
            name = "World"
            
        print(f"Hello, {name}!")