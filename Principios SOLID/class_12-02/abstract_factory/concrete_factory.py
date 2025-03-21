from abstract_factory import Button, UIAbstractFactory, TextBox

class DarkButton(Button):
    def paint(self):
        print("Dark button")

class DarkTextBox(TextBox):
    def paint(self):
        print("Dark textbox")

class LightButton(Button):
    def paint(self):
        print("Light button")

class LightTextBox(TextBox):
    def paint(self):
        print("Light textbox")

class DarkUIFactory(UIAbstractFactory):
    def create_button(self):
        return DarkButton()
    
    def create_textbox(self):
        return DarkTextBox()
    
class LightUIFactory(UIAbstractFactory):
    def create_button(self):
        return LightButton()
    
    def create_textbox(self):
        return LightTextBox()
