from ppip_function import ppip 

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
    def __init__(self,x,y):
        light_intensity = 60
        temperature = 10
        distance = 2.5
        self.x = 0
        self.y = 0


plants=[]
def ppip(length_p, width_p, d):
    global plants
    i=j=k=l=0
    while True:
        if j == 0 and i+(2*d) > length_p:
            break 
        if j > 0 and i + (2*d) > length_p:
            break
        if j == 0:
            k=l=0
            i+= 2*d
            j+=1
            while True:
                if l == 0 and k+(2*d) > width_p:
                    break
                if l > 0 and k+(2*d)> width_p:
                    break
                if l == 0:
                    k+= 2*d
                    l+=1
                else:
                    k+=d
                    l+=1
                plants.append(Carrot(x=i,y=k))
        else:
            k=l=0
            i+=d
            j+=1
            while True:
                if l == 0 and k+(2*d) > width_p:
                    break
                if l > 0 and k+(2*d)> width_p:
                    break
                if l == 0:
                    k+= 2*d
                    l+=1
                else:
                    k+=d
                    l+=1
                plants.append(Carrot(x=i,y=k))
    print(plants)


ppip(100,10,2)
print("What would you like to grow?")
userinput=input()

