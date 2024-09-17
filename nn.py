import math
# import keyboard

# if __name__ == "__main__":
#     print("hello world")
#     keyboard.wait('esc')


class Block():
    def __init__(self, title):
        self.title = title
        self.content = []
    
    def  add_content(self, text):
        self.content.append(text)

    def display(self):
        print(f"{'_'*50}")
        print(f"|{self.title.center(48)}|")
        print(f"|{'-'*48}|")
        for line in self.content:
            print(f"| {line.ljust(47)}|")
        print(f"|{'_'*48}|")











