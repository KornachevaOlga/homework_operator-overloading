class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'{self.name}, {self.number_of_floors}'
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
        isinstance(other, int)



    def __add__(self, value):#value
        #if 1 <= value >= self.number_of_floors:
        #while 1 > 0:
            #for i in range(number_of_floors + 1):
                #print(f'Этаж {i}')
            #break
            return self.number_of_floors +value
    def __radd__(self, value):
        return self.number_of_floors +value
    def __iadd__(self, value):
        return self.number_of_floors + value

h1 = House('ЖК Эльбрус', 20)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
print(str(h1))
print(str(h2))
print(h1 == h2)

print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)
print(h1.__add__(2))
print(h1.__add__(23))
print(h1.__radd__(2))
print(h2.__iadd__(5))
