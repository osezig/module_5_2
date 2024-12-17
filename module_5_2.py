class House:
    def __init__(self, name, number_of_floor):
        self.new_floor = None
        self.name = name
        self.number_of_floor = int(number_of_floor)
    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        for i in range(1, new_floor):
            print(i)
        if new_floor > self.number_of_floor or new_floor < 1:
            print('-Такого этажа не существует-')
        else:
            print(f'Мы поедем на {new_floor} этаж')
            
            # Домашняя работа по уроку "Специальные методы классов"
    def __len__(self):# - должен возвращать кол-во этажей здания self.number_of_floors.
        return self.number_of_floor
    def __str__(self):# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>"
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floor}"
H1 = House('ЖК Кирпичи', '23')
print(f'Название объекта недвижимости - {H1.name}, этажность здания - {H1.number_of_floor}')
H1.go_to(12)
# __str__
print(H1)
# __len__
print(len(H1))





