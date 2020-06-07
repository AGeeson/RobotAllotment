from ppip_function import pip, plants, ppip
from tkinter import Tk, Canvas, Frame, BOTH

class Vegetable:

    family = "plant"
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
        
carrot = Vegetable("Carrot", 5)
potato = Vegetable("Potato", 3)
basil = Vegetable("Basil", 7)

print(carrot.distance)
ppip(100,10, 2)

distance = 2
width = 10
length = 100

bounds=[0,width,length,0]


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Colours")
        self.pack(fill=BOTH,expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(0,5*width,5*length,0,
        outline="#fb0", fill="#fb0")
        for plant in plants:
            canvas.create_bitmap(5*plant["x"],5*plant["y"],bitmap="warning")
        canvas.pack(fill=BOTH, expand=1)

def main():
    root = Tk()
    ex = Example()
    root.mainloop()

if __name__ == '__main__':
    main()




