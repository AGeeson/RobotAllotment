

class Plant:
    def __init__(self, name, light_intensity, temperature, distance):
        self.name = name
        self.light_intensity = 0
        self.temperature = 0
        self.distance = 0
        self.depth = 0
        self.x=0
        self.y=0

class Carrot(Plant):
    def __init__(self):
        light_intensity = 60
        temperature = 10
        distance = 2.5
        self.x = 0
        self.y = 0



class Point(Carrot):
    def __init__(self):
        self.plant = plant
        self.x = 0
        self.y = 0

plant=[]
for q in range(10):
    a=1
    b=2
    q = Carrot()
    q.x = a
    q.y = b
    plant.append(q)
    a+=1
    b+=1
    




print(plant)
print(plant[0].x, plant[0].__class__)