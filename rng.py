#small practice for a generator
import random

def rng(num_max):
    while True:
        yield random.randrange(0, num_max)

class random_object:
    def __init__(self, weight, name):       #weight here means weighting for the calculations of the end result
        self.weight = weight
        self.name = name
    


def main():
    shoe = random_object(100, "shoe")           #some objects to return with different weighting 
    box = random_object(200, "Cardboard Box")
    shirt = random_object(10, "Shirt")

    sele = list()
    sele.append(shoe)
    sele.append(box)
    sele.append(shirt)
    count = 0

     
    for i in rng(shoe.weight + box.weight + shirt.weight):
        for x in sele:
            if i <= x.weight:
                print(x.name)
                break
            else:
                i -= x.weight
        break


if __name__ == "__main__":
    main()
