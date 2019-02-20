from tkinter import *
from pop import *

class screen(object):
    def __init__(self, parent):
        self.parent = parent
        self.wait_time = 10
        self.width = 600 
        self.height = 600 
        self.frame = Frame(parent)
        self.frame.pack()
        self.canvas = Canvas(self.frame, background="white", width=self.width, height=self.height)
        self.canvas.pack()
        self.pop = Pop(500)
    
    def draw(self):
        self.canvas.delete("all")
        for i in range(len(self.pop.dot_pop)):
            bounding_box = (self.pop.dot_pop[i].p[0]-self.pop.dot_pop[i].rad, \
                            self.pop.dot_pop[i].p[1]-self.pop.dot_pop[i].rad,\
                            self.pop.dot_pop[i].p[0]+self.pop.dot_pop[i].rad, \
                            self.pop.dot_pop[i].p[1]+self.pop.dot_pop[i].rad) 
            bounding_box1 = (self.pop.dot_pop[i].p[0]-self.pop.dot_pop[i].rad*2, \
                            self.pop.dot_pop[i].p[1]-self.pop.dot_pop[i].rad*2,\
                            self.pop.dot_pop[i].p[0]+self.pop.dot_pop[i].rad*2, \
                            self.pop.dot_pop[i].p[1]+self.pop.dot_pop[i].rad*2)             
            if self.pop.dot_pop[i].best is True:
                self.canvas.create_oval(bounding_box, fill='orange')
            else:
                self.canvas.create_oval(bounding_box, fill='black')
        self.canvas.create_oval(295,0,305,10, fill='red') #CHANGE FOR GOALS
        #self.canvas.create_rectangle(0,400,450,420, fill='blue') #THESE ARE THE OBSTACLES
        #self.canvas.create_rectangle(150,280,600,300, fill='blue') 
        #self.canvas.create_rectangle(0,160,450,180, fill='blue')
        #self.canvas.create_rectangle(100,290,500,310, fill='blue')                 
        self.canvas.update()        
        self.canvas.after(self.wait_time)

    def up(self):
        for i in range(len(self.pop.dot_pop)):
            if self.pop.dot_pop[i].p[0]-self.pop.dot_pop[i].rad <= 0 or self.pop.dot_pop[i].p[1]-self.pop.dot_pop[i].rad <= 0 or \
               self.pop.dot_pop[i].p[0]+self.pop.dot_pop[i].rad >= self.width or self.pop.dot_pop[i].p[1]+self.pop.dot_pop[i].rad >= self.height:
                self.pop.dot_pop[i].out = True
            if (295 <= self.pop.dot_pop[i].p[0] - 2 <= 305 or 295 <= self.pop.dot_pop[i].p[0] + 2 <= 305\
                ) and (0 <= self.pop.dot_pop[i].p[1] - 2 <= 10 or 0 <= self.pop.dot_pop[i].p[1] + 2<= 10):
                self.pop.dot_pop[i].out = True
                self.pop.dot_pop[i].goal = True
            if self.pop.dot_pop[i].m.step > self.pop.fast:
                self.pop.dot_pop[i].out = True
            #THIS IS FOR OBSTACLE COLLISION
            #self.pop.dot_pop[i].col_test(0,400,450,420)
            #self.pop.dot_pop[i].col_test(150,280,600,300)
            #self.pop.dot_pop[i].col_test(0,160,450,180)
            #self.pop.dot_pop[i].col_test(100,290,500,310)
    
    def animate(self):
        tot = 1
        while tot > 0:
            tot = 0
            self.draw()
            for i in range(len(self.pop.dot_pop)):
                if self.pop.dot_pop[i].out is False:
                    self.pop.dot_pop[i].move()
            self.up()
            for i in range(len(self.pop.dot_pop)):
                if self.pop.dot_pop[i].out == False:
                    tot += 1   
            
        

if __name__ == "__main__":
    goal = (300, 5)
    root = Tk()
    root.title('Learning Machine Learning')
    scene = screen(root)
    while True:
        scene.animate()
        scene.pop.selection()
        scene.pop.mut()
        print(scene.pop.fast)
    root.mainloop()

