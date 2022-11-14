from manim import *

class AnimateDot(Scene):
    def construct(self):
        dot = Dot()
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(DOWN))
        self.play(dot.animate.shift(LEFT))
        self.play(dot.animate.shift(RIGHT))

class CreateDot(Scene):
    def construct(self):
        dot = Circle()
        self.play(Create(dot))
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(DOWN))
        self.play(dot.animate.shift(LEFT))
        self.play(dot.animate.shift(RIGHT))
        self.play(Uncreate(dot))

class GrowCircle(Scene):
    def construct(self):
        circle = Circle()
        self.play(GrowFromCenter(circle))
        self.play(Uncreate(circle))

class FadeCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(RED,opacity=1)
        self.play(FadeIn(circle))
        self.play(Uncreate(circle))



class AnimateSquare(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        #self.add(square)

        # animate the change of color
        self.play(square.animate.set_fill(WHITE))
        self.wait(1)

        # animate the change of position and the rotation at the same time
        self.play(square.animate.shift(UP).rotate(PI / 3))
        self.wait(1)


class TraceDot(Scene):
    def construct(self):
        a = Dot(RIGHT * 2)

        b = TracedPath(a.get_center, stroke_opacity=[1,0])
        
        self.add(a,b)
        self.play(a.animate.shift(LEFT * 2))
        self.play(a.animate.shift(RIGHT * 2))
        self.wait()