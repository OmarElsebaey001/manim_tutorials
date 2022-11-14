from manim import *

class s(Scene):
    def construct(self):
        d = Dot()
        trace = TracedPath(d.get_center)
        self.add(trace, d)
        self.play(d.animate.shift(UP))
        for i in range(10):
            self.play(d.animate().rotate(PI/4,about_point=[0,0,0]))
        self.play(d.animate.shift(UP))
        for i in range(10):
            self.play(d.animate().rotate(PI/4,about_point=[0,0,0]))
        self.play(d.animate.shift(UP))
        for i in range(10):
            self.play(d.animate().rotate(PI/4,about_point=[0,0,0]))
        #self.play(d.animate.shift(UP))
        #for i in range(6):
        #    self.play(d.animate().rotate(PI/4,about_point=[0,0,0]))
        self.play(d.animate.shift(RIGHT))
        self.play(d.animate.shift(LEFT))