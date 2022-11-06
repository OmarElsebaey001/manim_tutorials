from manim import *
#https://docs.manim.community/en/stable/reference.html#mobjects

class AddCircle(Scene):
    def construct(self):
        print("Current objects in the scene: ",self.mobjects)
        circle = Circle()
        self.add(circle)
        self.wait(1)
        print("Current objects in the scene: ",self.mobjects)

class CircleProperties(Scene):
    def construct(self):
        circle = Circle()
        circle.color = GREEN
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
        triangle_1.shift(UP)
        self.add(triangle_1)