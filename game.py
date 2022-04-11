import tkinter as tk
import random
class Rabbit_turtle_race():
    def __init__(self):
        self.window = tk.Tk()

        # canvas
        self.canvas= tk.Canvas(master=self.window, width=600, height=600, bg='lightgreen')
        self.canvas.pack(fill=tk.BOTH, expand= True)

        # create line
        self.canvas.create_line(65, 147, 65, 475, fill='red')
        self.canvas.create_line(535, 147, 535, 475, fill='green')

        self.turtle_coord=[33,206]
        self.rabbit_coord=[33,400]
        self.no_of_booster=3
        self.finish_x=535
        self.end=False
        # load the image
        im_turtle=tk.PhotoImage(file= 'd:/turtle.png')
        im_rabbit = tk.PhotoImage(file='d:/rabbit.png')

        # render it on the canvas
        self.turtle=self.canvas.create_image(self.turtle_coord, image=im_turtle)
        self.rabbit = self.canvas.create_image(self.rabbit_coord, image=im_rabbit)

        #bind the key
        self.window.bind('<Right>', self.right_moves)
        self.window.after(50,self.rabbit_moves)
        self.window.bind('<Control-Right>', self.booster_use)

        self.window.mainloop()

    def race_end(self):
        if self.rabbit_coord[0]>=self.finish_x:
            print('rabbit has won the race')
            self.end=True
            self.window.unbind('<Right>')
            self.window.unbind('<Control-Right>')

        elif self.turtle_coord[0]>=self.finish_x:
            print('turtle has won the race')
            self.end=True
            self.window.unbind('<Right>')
            self.window.unbind('<Control-Right>')


    def right_moves(self, event):
        self.turtle_coord[0] += 5
        self.canvas.coords(self.turtle, self.turtle_coord)
        self.race_end()



    def rabbit_moves(self):
       self.rabbit_coord[0]+= random.randint(1, 10)
       self.canvas.coords(self.rabbit, self.rabbit_coord)
       #print('amit')
       self.race_end()
       if not self.end:
           self.window.after(50,self.rabbit_moves)

    def booster_use(self, event):
        if self.no_of_booster> 0:
            jump=35
            self.no_of_booster-=1
        else:
            jump=5
            self.no_of_booster-=1

        self.turtle_coord[0]+=jump
        self.canvas.coords(self.turtle, self.turtle_coord)
        self.race_end()


Rabbit_turtle_race()
