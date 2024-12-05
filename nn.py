import textwrap

class Block:
    def __init__(self, title):
        self.title = title
        self.content = []

    def add_content(self, line):

        #Add a line of content to the block.

        self.content.append(line)

    def render(self, width=50):

        #Render block with the specified width.

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











