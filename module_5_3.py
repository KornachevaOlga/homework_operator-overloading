class House:
    houses_history = []

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'{self.name}, {self.number_of_floors}'
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    # def __lt__(self, other):
    #     return self.number_of_floors < other.number_of_floors
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)
    # def __gt__(self, other):
    #     return self.number_of_floors > other.number_of_floors

    def __gt__(self, other):
        return not self.__le__(other)
    # def __ge__(self, other):
    #     return self.number_of_floors >= other.number_of_floors

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)


    # def __ne__(self, other):
    #     return self.number_of_floors != other.number_of_floors
    #     isinstance(other, int)



    def __add__(self, value):#value
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        return self

    # def __radd__(self, value):
    #     return self.number_of_floors +value
    def __radd__(self, other):
        return self.__add__(other)
    # def __iadd__(self, value):
    #     return self.number_of_floors + value
    def __iadd__(self, other: int):
        return self.__add__(other)


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
h1 += 10 #(метод вызывается, когда используется оператор +=)
h2 = 10 + h2 #(метод вызывается, когда объект находится справа от оператора +,
                # и левый операнд не поддерживает операцию сложения с ним)
