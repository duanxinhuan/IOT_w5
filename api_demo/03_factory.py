# Reference: https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_factory.htm
class Button():
    def __init__(self):
        self.html = ""
    
    def get_html(self):
        return self.html

class Image(Button):
    def __init__(self):
        super().__init__()
        self.html = "<img></img>"

class Input(Button):
    def __init__(self):
        super().__init__()
        self.html = "<input></input>"

class Flash(Button):
    def __init__(self):
        super().__init__()
        self.html = "<obj></obj>"

class ButtonFactory():
    def create_button(self, type):
        target_class = type.capitalize()
        #convert the first to upper 
        return globals()[target_class]()
        #return the class generated
        #globals() give a class name the  create a object, the string is a key, calling () to construt a class
button_factory = ButtonFactory()
button = ["image", "input", "flash"]
for b in button:
    print(button_factory.create_button(b).get_html())
