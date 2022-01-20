class Data:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if type(other) == int:
            return Data(self.value + other)

    def __sub__(self, other):
        if type(other) == int:
            return Data(self.value - other)


data = Data(5)

new_value = data + 10 - 3

print(new_value.value)

