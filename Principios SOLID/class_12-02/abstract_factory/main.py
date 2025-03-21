from concrete_factory import DarkUIFactory
from concrete_factory import LightUIFactory

def client_code(factory):
    button = factory.create_button()
    textbox = factory.create_textbox()
    button.paint()
    textbox.paint()

if __name__ == "__main__":
    client_code(DarkUIFactory())
    print()
    client_code(LightUIFactory())