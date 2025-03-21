from component import Text

class PlainText(Text):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text