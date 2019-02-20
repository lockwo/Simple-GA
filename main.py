from main_canvas import *
from tkinter import *

root = Tk()
root.title('Learning Machine Learning')
scene = screen(root)
for j in range(500):
    scene.animate()
    scene.pop.selection()
    scene.pop.mut()
    print(j + 1, scene.pop.fast)
root.mainloop()
