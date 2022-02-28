'''
A class is a structure that allows you to combine the data and functionality associated with a particular task. The variables of a class are attributes. The functions of a class are methods.
'''
class Arithmetic:

    def __init__(self, number1 = 10, number2 = 20):
        # Idea behind this logic is to ensure number2 is greater or equal to number1.
        if(number1 > number2):
            self.number2 = number1
            self.number1 = number2
        else:
            self.number1 = number1
            self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number2 - self.number1

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return self.number2 / self.number1

    def remainder(self):
        return self.number2 % self.number1

    def print_self(self):
        print(self)
