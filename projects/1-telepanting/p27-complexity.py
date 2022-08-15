from common import *
from core import *
from manim import *

class p27(Scene):
    def construct(self):
        self.wait()
        w = MathTex("O(N^2)",font_size=128)
        self.play( Write(w) )
        self.wait()
        self.play( Unwrite(w) )
        self.wait()

        w = MathTex(r"O(N \,log\, N)", font_size=128)
        self.play( Write(w) )
        self.wait()
        self.play( Unwrite(w) )
        self.wait()
