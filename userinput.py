from ppip_function import pip, plants, ppip
from tkinter import Tk, Canvas, Frame, BOTH


vegetables = [
    {"carrot": 1},
    {"potato": 2},
    {"cabbagge":3},
    {"rosemary":4}
]
picked=[]
print("what would you like to grow? \n1. Potato \n2. Cabbage \n3. Carrot \n4. Rosemary \nEnter the number of one of them separated by commas")
userinput=input()
x=userinput.split(",")
print(x)
for r in x:
    s=int(r)
    picked.append(vegetables[s])
print("What are the dimensions of your allotment. Format: x,y")
widthinput=input("width:")
print (widthinput)
width = float(widthinput)
"""if widthinput != type(float) or type(int):
    print("error: value must be integer or float")"""
heightinput=input("height:")
height = float(heightinput)
"""if heightinput != type(float) or type(int):
    print("error: value must be integer or float")"""
# for key in picked:
  #  minimum_amount = input("Is there a maximum number of " + key )

ppip(height,width,2.5)

bounds=[0,width,height,0]

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Colours")
        self.pack(fill=BOTH,expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(0,5*width,5*height,0,
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




