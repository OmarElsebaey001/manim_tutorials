from manim import *

class Runtime(Scene):
    def construct(self):
        a = Dot()
        self.play(a.animate(run_time=4).shift(RIGHT))
        self.play(a.animate(run_time=2).shift(RIGHT))
        self.play(a.animate(run_time=1).shift(RIGHT))

class CenterTracer(Scene):
    def construct(self):
        a = Circle()
        
        trace = TracedPath(a.get_center)
        self.add(trace)

        self.play(a.animate.shift(RIGHT))
        self.play(a.animate.shift(UP))
        self.play(a.animate.shift(LEFT))
        self.play(a.animate.shift(DOWN))

class SquareTracer(Scene):
    def construct(self):
        a = Square()
        a.set_stroke(opacity=0.1)
        
        
        trace = TracedPath(traced_point_func=a.get_top,stroke_color=RED)
        self.add(trace)

        self.play(a.animate.shift(RIGHT))
        self.play(a.animate.shift(UP))
        self.play(a.animate.shift(LEFT))
        self.play(a.animate.shift(DOWN))


class DifferentAnimateMethods(Scene):
    def construct(self):
        a = Dot()
        
        trace = TracedPath(a.get_center)
        self.add(trace)

        self.play(a.animate.shift(UP))
        self.play(a.animate.rotate(angle=PI/2,about_point=[0,0,0]))

        self.play(a.animate.shift(RIGHT))
        self.play(a.animate.shift(UP))
        
        self.play(Rotate(a,angle=PI/2,about_point=[0,0,0]))

class MultiplAnimations(Scene):
    def construct(self):
        d0 = Dot()
        d1 = Dot()

        self.play(d0.animate.shift(LEFT),d1.animate.shift(RIGHT))
        self.play(d0.animate.shift(RIGHT),d1.animate.shift(LEFT))

class MultiplAnimationsDifferentTimings(Scene):
    def construct(self):
        d0 = Dot()
        d1 = Dot()

        self.play(d0.animate(run_time=1).shift(LEFT),d1.animate(run_time=2).shift(RIGHT))

class Grouping(Scene):
    def construct(self):
        d0 = Dot()
        c0 = Circle()
        group0 = Group(d0,c0)
        self.play(group0.animate.shift(UP))

class VGrouping(Scene):
    def construct(self):
        d0 = Dot()
        s0 = Square()
        group0 = VGroup(d0,s0)
        self.play(Create(group0))
        self.play(group0.animate.shift(UP))
        self.play(Rotate(group0,angle=PI))
        self.play(group0.animate.shift(DOWN))
        

with tempconfig({"quality": "medium_quality", "preview": True}):
    scene = SquareTracer()
    scene.render()