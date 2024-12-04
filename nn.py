# import math
# import keyboard

# # if __name__ == "__main__":
# #     print("hello world")
# #     keyboard.wait('esc')


# class Block():
#     def __init__(self, title):
#         self.title = title
#         self.content = []
    
#     def  add_content(self, text):
#         self.content.append(text)

#     def display(self):
#         print(f"{'_'*80}") #50
#         print(f"|{self.title.center(48)}|")
#         print(f"|{'-'*78}|") #48
#         for line in self.content:
#             print(f"| {line.ljust(47)}|")
#         print(f"|{'_'*78}|") #48

import textwrap

class Block:
    def __init__(self, title):
        self.title = title
        self.content = []

    def add_content(self, line):
        """
        Add a line of content to the block.
        """
        self.content.append(line)

    def render(self, width=50):
        """
        Render the block as a string with the specified width.
        """
        border = "_" * width
        divider = "|" + "-" * (width - 2) + "|"

        # Wrapped content
        wrapped_content = []
        for line in self.content:
            wrapped_content.extend(textwrap.wrap(line, width=width - 4))

        # Render the block
        rendered = [border]
        rendered.append(f"| {self.title.center(width - 4)} |")
        rendered.append(divider)
        for line in wrapped_content:
            rendered.append(f"| {line.ljust(width - 4)} |")
        rendered.append(border)
        return "\n".join(rendered)











