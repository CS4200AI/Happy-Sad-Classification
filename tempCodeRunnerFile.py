import math
import tkinter as tk

class RotatingCube(tk.Canvas):
    def __init__(self, parent, size):
        tk.Canvas.__init__(self, parent, width=size, height=size)
        self.size = size
        self.cube_size = size * 0.8
        self.cube_center = size / 2
        self.angle = 0
        self.cube_vertices = [
            (self.cube_center - self.cube_size / 2, self.cube_center - self.cube_size / 2, self.cube_center - self.cube_size / 2),
            (self.cube_center + self.cube_size / 2, self.cube_center - self.cube_size / 2, self.cube_center - self.cube_size / 2),
            (self.cube_center + self.cube_size / 2, self.cube_center + self.cube_size / 2, self.cube_center - self.cube_size / 2),
            (self.cube_center - self.cube_size / 2, self.cube_center + self.cube_size / 2, self.cube_center - self.cube_size / 2),
            (self.cube_center - self.cube_size / 2, self.cube_center - self.cube_size / 2, self.cube_center + self.cube_size / 2),
            (self.cube_center + self.cube_size / 2, self.cube_center - self.cube_size / 2, self.cube_center + self.cube_size / 2),
            (self.cube_center + self.cube_size / 2, self.cube_center + self.cube_size / 2, self.cube_center + self.cube_size / 2),
            (self.cube_center - self.cube_size / 2, self.cube_center + self.cube_size / 2, self.cube_center + self.cube_size / 2),
        ]
        self.draw_cube()

    def draw_cube(self):
        x1 = self.cube_center - self.cube_size / 2
        y1 = self.cube_center - self.cube_size / 2
        x2 = self.cube_center + self.cube_size / 2
        y2 = self.cube_center + self.cube_size / 2

        # draw bottom face
        self.create_line(x1, y1, x2, y1)
        self.create_line(x2, y1, x2, y2)
        self.create_line(x2, y2, x1, y2)
        self.create_line(x1, y2, x1, y1)
