class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec

    def __str__(self) -> str:
        return f'{self.name}, возраст: {self.age}, голос: {self.spec}'


class Dog(Animal):
    def __init__(self, type_a, name, age, spec):
        super().__init__(name, age)
        self.spec = spec
        self.type = type_a

    def __str__(self):
        return self.type + ' ' + super().__str__()


class Bird(Animal):
    def __init__(self, type_a, name, age, spec):
        super().__init__(name, age)
        self.spec = spec
        self.type = type_a

    def __str__(self):
        return self.type + ' ' + super().__str__()


class Fish(Animal):
    def __init__(self, type_a, name, age, spec):
        super().__init__(name, age)
        self.spec = spec
        self.type = type_a

    def __str__(self):
        return self.type + ' ' + super().__str__()


class Factory:
    def __init__(self, *args):
        self.type, *opt = args
        self.options = opt
        self.new_instance = self.create_instance()

    def create_instance(self):
        name, age, voice, *_ = self.options
        if self.type == 'Dog':
            self.new_instance = Dog('Собака', name, age, voice)
        if self.type == 'Bird':
            self.new_instance = Bird('Птица', name, age, voice)
        if self.type == 'Fish':
            self.new_instance = Fish('Рыба', name, age, voice)
        return self.new_instance

    def __str__(self):
        return self.new_instance.__str__()


if __name__ == '__main__':
    animal_farm = [
        ['Dog', 'Muxtar', 5, 'gaff'],
        ['Bird', 'Roger', 2, 'karr'],
        ['Fish', 'Ixtiandr', 100, 'adyou'],
    ]
    for animal in animal_farm:
        new_animal = Factory(*animal)
        print(new_animal)
