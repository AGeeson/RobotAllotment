from tkinter import *
from tkinter.ttk import *

window = Tk()

window.geometry('1000x300')

window.title("Robot Allotment")

dimension_label = Label(window, text="Dimensions")
height_d_label = Label(window, text="H")
width_d_label = Label(window, text="W")
height_entry = Entry(window, width=10)
width_entry = Entry(window, width=10)
plant_label = Label(window, text="Plants")
plant_label2 = Label(window, text="How many? Up to 5")
number_of_plants_combo = Combobox(window)
number_of_plants_combo['values']=(1,2,3,4,5)
number_of_plants_combo.current(1)

#error messages
h_error = Label(window, text="")
w_error = Label(window, text="")

dimension_label.grid(row=0, column=0)
height_d_label.grid(column=0, row=1)
width_d_label.grid(column=2, row=1)
height_entry.grid(column=1, row=1)
width_entry.grid(column=3, row=1)
plant_label.grid(column=0, row=3)
plant_label2.grid(column=0, row=4)
number_of_plants_combo.grid(column=0, row=5)

plant_options = ('Carrot', 'Basil', 'Potato')

#Plant 1
p1_label = Label(window, text="P1")
p1_plant_choice = Combobox(window)
p1_plant_choice['values'] = plant_options
p1_minmax = Combobox(window)
p1_minmax['values'] = ('Min','Max', "Min/Max")
p1_percorhash = Combobox(window)
p1_percorhash['values'] = ('%','#')
p1_minmax_amount = Entry(window, width='10')

p1_label.grid(column=0, row=6)
p1_plant_choice.grid(column=0, row=7)
p1_minmax.grid(column=0, row=8)
p1_percorhash.grid(column=0, row=9)
p1_minmax_amount.grid(column=0, row=10)

#Plant 2
p2_label = Label(window, text="P2")
p2_plant_choice = Combobox(window)
p2_plant_choice['values'] = plant_options
p2_minmax = Combobox(window)
p2_minmax['values'] = ('Min','Max')
p2_percorhash = Combobox(window)
p2_percorhash['values'] = ('%','#')
p2_minmax_amount = Entry(window, width='10')

p2_label.grid(column=1, row=6)
p2_plant_choice.grid(column=1, row=7)
p2_minmax.grid(column=1, row=8)
p2_percorhash.grid(column=1, row=9)
p2_minmax_amount.grid(column=1, row=10)

#Plant 3
p3_label = Label(window, text="P3")
p3_plant_choice = Combobox(window)
p3_plant_choice['values'] = plant_options
p3_minmax = Combobox(window)
p3_minmax['values'] = ('Min','Max')
p3_percorhash = Combobox(window)
p3_percorhash['values'] = ('%','#')
p3_minmax_amount = Entry(window, width='10')

p3_label.grid(column=2, row=6)
p3_plant_choice.grid(column=2, row=7)
p3_minmax.grid(column=2, row=8)
p3_percorhash.grid(column=2, row=9)
p3_minmax_amount.grid(column=2, row=10)

#Plant 4
p4_label = Label(window, text="P4")
p4_plant_choice = Combobox(window)
p4_plant_choice['values'] = ('Carrot', 'Turnip', 'Courgette', 'Cabbage', 'Potato', "Text")
p4_minmax = Combobox(window)
p4_minmax['values'] = ('Min','Max')
p4_percorhash = Combobox(window)
p4_percorhash['values'] = ('%','#')
p4_minmax_amount = Entry(window, width='10')

p4_label.grid(column=3, row=6)
p4_plant_choice.grid(column=3, row=7)
p4_minmax.grid(column=3, row=8)
p4_percorhash.grid(column=3, row=9)
p4_minmax_amount.grid(column=3, row=10)

#Plant 5
p5_label = Label(window, text="P5")
p5_plant_choice = Combobox(window)
p5_plant_choice['values'] = ('Carrot', 'Turnip', 'Courgette', 'Cabbage', 'Potato', "Text")
p5_minmax = Combobox(window)
p5_minmax['values'] = ('Min','Max')
p5_percorhash = Combobox(window)
p5_percorhash['values'] = ('%','#')
p5_minmax_amount = Entry(window, width='10')

p5_label.grid(column=4, row=6)
p5_plant_choice.grid(column=4, row=7)
p5_minmax.grid(column=4, row=8)
p5_percorhash.grid(column=4, row=9)
p5_minmax_amount.grid(column=4, row=10)

#Plants Class
class Vegetable:

    family = "plant"
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
        
Carrot = Vegetable("Carrot", 5)
potato = Vegetable("Potato", 3)
basil = Vegetable("Basil", 7)

plants = [Carrot, potato, basil]
#Buttons
def visualise():
    p1 = ""
    p2 = ""
    newWindow = Toplevel(window)
    newWindow.title("Visualised allotment")
    newWindow.geometry("200x200")
    Label(newWindow, text="This is a new window")
    canvas = Canvas(newWindow)
    canvas.create_rectangle(0,5*float(height_entry.get()), 5*float(width_entry.get()),0,
        outline="#fb0", fill="#fb0")
    canvas.pack(fill=BOTH, expand=1)
    for plant in plants:
        if p1_plant_choice.get() == plant:
            p1 = plant
    print(p1)


    # plant_1 = p1_plant_choice.get()
    # canvas.create_rectangle(0,5*height_entry.get(), 5*width_entry.get(), 0, 
    # outline="#fb0", fill="#fb0")

def save():
    pass

button_visualise = Button(window, text="Visualise", command=visualise)
button_save = Button(window, text="Save", command=save)
button_visualise.grid(column=0, row=12)
button_save.grid(column=1, row=12)



window.mainloop()