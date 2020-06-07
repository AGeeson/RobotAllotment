def pip(length_p, width_p, d):
    i=j=k=l=0
    while True:
        if i+(2*d) > length_p:
            break 
        if j == 0:
            i+= 2*d+d
            j+=1
        else:
            i+=2*d
            j+=1
    excess_l = length_p - i

    while True:
        if k+(2*d) > width_p:
            break
        if l == 0:
            k+= 2*d+d
            l+=1
        else:
            k+=2*d
            l+=1
    excess_w = width_p - k
    total_excess = excess_w+j + excess_l*l
    area = length_p*width_p
    percent_excess = (total_excess/area)*100
    print("Possible points in polygon is: " + str(l*j))
    print("with excess space of: "  + str(total_excess) + "cmxcm or " + str(percent_excess) )

class Vegetable:

    family = "plant"
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
        
carrot = Vegetable("Carrot", 5)
potato = Vegetable("Potato", 3)
basil = Vegetable("Basil", 7)

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
                plants.append({
                    "x": i ,
                    "y": k})
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
                plants.append({
                    "x": i ,
                    "y": k})
    print(plants)
