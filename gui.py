import math
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from tkinter import filedialog, Label, Toplevel
import tensorflow as tf
import cv2
import numpy as np
from matplotlib import pyplot as plt


class RotatingCube(tk.Canvas):
    def __init__(self, parent, size):
        tk.Canvas.__init__(self, parent, width=size, height=size, highlightbackground='black')
        self.size = size
        self.cube_size = size * 0.2
        self.cube_center = size / 2
        self.angle = 0
        self.draw_cube()
        self.configure(bg='black')

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

        # draw top face
        self.create_line(x1, y1 - self.cube_size / 3, x2, y1 - self.cube_size / 3)
        self.create_line(x2, y1 - self.cube_size / 3, x2, y2 - self.cube_size / 3)
        self.create_line(x2, y2 - self.cube_size / 3, x1, y2 - self.cube_size / 3)
        self.create_line(x1, y2 - self.cube_size / 3, x1, y1 - self.cube_size / 3)

        # draw vertical lines
        self.create_line(x1, y1, x1, y1 - self.cube_size / 3)
        self.create_line(x2, y1, x2, y1 - self.cube_size / 3)
        self.create_line(x2, y2, x2, y2 - self.cube_size / 3)
        self.create_line(x1, y2, x1, y2 - self.cube_size / 3)
    def rotate_cube(self):
        self.angle = 1
        if self.angle > 359:
            self.angle = 0
        radian = math.radians(45+self.angle)
        cos_val = math.cos(radian)
        sin_val = math.sin(radian)
        for i in self.find_all():
            x, y = self.coords(i)[:2]
            x -= self.cube_center
            y -= self.cube_center
            new_x = x * cos_val - y * sin_val
            new_y = x * sin_val + y * cos_val
            self.coords(i, new_x + self.cube_center, new_y + self.cube_center, *self.coords(i)[2:])

        self.after(100, self.rotate_cube)
class results(tk.Canvas):
    def __init__(self, parent, size):
        tk.Canvas.__init__(self, parent, width=size, height=size)
        self.size = size
    def open(self):
        global image
        filetypes = [("JPEG files" , "*.jpg")]
        root.filename = filedialog.askopenfilename(initialdir='C:\\Users\\', filetypes=filetypes)
        orgimage = Image.open(root.filename)
        orgimage.thumbnail((600,600))
        image = ImageTk.PhotoImage(orgimage)
        nextpage = Toplevel(root)
        nextpage.title('Prediction')
        nextpage.geometry("800x1000")
        nextpage.configure(bg='black')

        image_label = Label(nextpage, image = image).pack()

        customtkinter.set_appearance_mode("Dark")
        # customtkinter.set_default_color_theme("b")
        cancelbutton = customtkinter.CTkButton(nextpage, text = "Return", command = nextpage.destroy)
        cancelbutton.pack()
        image_path = root.filename
        results.AIprediction(image_path, nextpage)
        

    def openHappy(nextpage):
        nextpage.configure(bg='darkgreen')
        happy = Label(nextpage, text='Happy').pack()

    def openSad(nextpage):
        nextpage.configure(bg='black')
        happy = Label(nextpage, text='Sad').pack()
    def AIprediction(image_path, nextpage):
        model = tf.keras.models.load_model('model')
        img = cv2.imread(image_path)
        plt.imshow(img)
        resize = tf.image.resize(img, (256,256))
        plt.imshow(resize.numpy().astype(int))  
        tf.function(
            func=None,
            input_signature=None,
            autograph=True,
            jit_compile=None,
            reduce_retracing=False,
            experimental_implements=None,
            experimental_autograph_options=None,
            experimental_attributes=None,
            experimental_relax_shapes=None,
            experimental_compile=None,
            experimental_follow_type_hints=None
        )
        yhat = model.predict(np.expand_dims(resize/255, 0))
        if yhat > 0.5: 
            results.openSad(nextpage)
        else:
            results.openHappy(nextpage)




if __name__ == '__main__':
    root = tk.Tk()
    root.title("HappyvsSad")
    root.geometry("800x600")
    root.configure(bg= 'black')
    cube = RotatingCube(root, 300)
    cube.configure(bg= 'black')
    cube.pack()
    cube.rotate_cube()
    
    
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("blue")
    button = customtkinter.CTkButton(root, text ="Insert Image", command = results(root, 400).open)
    button.pack()
    

    root.mainloop()
