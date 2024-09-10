class Vehicle:
    __COLOR_VARIANTS = ['Black', 'Green', 'Yellow' 'Red', ]
    def __init__(self, owner: str, model: str, engine_power: int, color: str,):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Model: {self.__model}'

    def get_horsepower(self):
        return f'Horsepower: {self.get_horsepower}'

    def get_color(self):
        return f'Color: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        self.__color = new_color
        if new_color.lower() in map(str.lower, self.__COLOR_VARIANTS):
            return new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 #(в седан может поместиться только 5 пассажиров)

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, engine_power, color)

# Текущие цвета __COLOR_VARIANTS = ['Black', 'Green', 'Yellow' 'Red',]
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()