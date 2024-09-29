class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor or new_floor < 1:
            print("Такого этажа не существует")
        else:
            new_floor += 1
            for i in range(1, new_floor):
                print(i)


h1 = House('ЖК Горский', 12)
h2 = House('Домик в деревне', 2)
h1.go_to(9)
h2.go_to(3)