from component import Text

class TextDecorator(Text):
    def __init__(self, text_component):
        self.text_component = text_component

    def render(self):
        return self.text_component.render()