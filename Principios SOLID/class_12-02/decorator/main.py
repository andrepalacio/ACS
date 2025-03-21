from concrete_component import PlainText
from concrete_decorator import HTMLTextDecorator

plain_text = PlainText('Hello, world!')
print("texto sin decorar: ", plain_text.render())

html_text = HTMLTextDecorator(plain_text)
print("texto decorado: ", html_text.render())