from manim import *

#Scene declaration -> class <scene_name> (Scene):
class AddSingleObject(Scene):
    #Manim would run this code to create the scene
    def construct(self):
        #Object
        circle = Circle()

        #Actions
        self.add(circle)
        self.wait(1)