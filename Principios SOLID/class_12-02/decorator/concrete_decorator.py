from decoratorP import TextDecorator

class HTMLTextDecorator(TextDecorator):
  def render(self):
    return f'<p>{self.text_component.render()}</p>'