from manim import *

class a0(Scene):
    def construct(self):
        dot = Dot()
        cir_0 = Circle()
        self.play(GrowFromCenter(cir_0))
        self.play(Create(dot))
        self.play(dot.animate.shift(RIGHT))
        self.play(Rotate(dot,angle=PI,about_point=[0,0,0]))
        self.play(Rotate(dot,angle=PI,about_point=[0,0,0]))
        self.play(dot.animate.shift(LEFT))
        self.play(Uncreate(cir_0))
        self.play(Uncreate(dot))