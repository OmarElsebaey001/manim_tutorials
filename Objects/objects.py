from manim import *
#https://docs.manim.community/en/stable/reference.html#mobjects
x = "text"
class AddCircle(Scene):
    def construct(self):
        print("Current objects in the scene: ",self.mobjects)
        circle = Circle()
        self.add(circle)
        self.wait(1)
        print("Current objects in the scene: ",self.mobjects)
        self.remove(circle)
        print("Current objects in the scene: ",self.mobjects)
        

class CircleProperties(Scene):
    def construct(self):
        circle = Circle()
        circle.color = RED
        circle.radius = 4
        self.add(circle)
        self.wait(2)
        print("CENTER: ====>",circle.get_center())

class AddRectanlge(Scene):
    def construct(self):
        rect = Rectangle(width=4.0, height=2.0)
        rect.color = BLUE_D
        rect.height = 6
        self.add(rect)

class AddTriangle(Scene):
    def construct(self):
        triangle_1 = Triangle()
        self.add(triangle_1)

class AddTriangleShift(Scene):
    def construct(self):
        triangle_1 = Triangle()
        self.add(triangle_1)
        i = X_AXIS
        j = Y_AXIS
        k = Z_AXIS
        vector = 3 * i + 4 * j + 5 * k 
        self.play(triangle_1.animate.shift( 10*k ))