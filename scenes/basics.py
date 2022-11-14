from manim import *

class EmptyScene(Scene):
    pass

class AddSingleObject(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(2)
        self.remove(circle)
        self.wait(1)
        
        


class AddRemoveSingleObject(Scene):
    def construct(self):
        #Object
        circle = Circle()
        
        #Action
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)

class AddRemoveTwoObjects(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.add(circle)
        self.wait(1)
        self.add(square)
        self.wait(1)
        self.remove(circle)
        self.wait(1)
        self.remove(square)
        self.wait(1)

class AddRemoveMultiObjects(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.add(circle)
        self.wait(1)
        self.add(square)
        self.wait(1)
        self.remove(circle)
        self.wait(1)
        self.remove(square)
        self.wait(1)


class TextScene(Scene):
    def construct(self):
        text = Text("Hello World!")
        self.add(text)
        self.wait(4)

class SoundScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        dot = Dot().set_color(GREEN)
        self.add_sound("click.wav")
        self.add(dot)
        self.wait()
        
        self.add_sound("click.wav")
        self.wait(3)
        dot.set_color(BLUE)
        self.wait()

        self.add_sound("click.wav")
        dot.set_color(RED)
        self.wait()