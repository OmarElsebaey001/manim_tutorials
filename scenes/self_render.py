from manim import * 
from manim.utils.file_ops import open_file as open_media_file 

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
    
if __name__ == '__main__':
    scene = AddRemoveMultiObjects()
    scene.render() # That's it!
    
    # Here is the extra step if you want to also open 
    # the movie file in the default video player 
    # (there is a little different syntax to open an image)
    open_media_file(scene.renderer.file_writer.movie_file_path)