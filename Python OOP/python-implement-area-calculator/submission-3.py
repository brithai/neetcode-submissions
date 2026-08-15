import math

class AreaCalc:
    # TODO: Implement calculate method
    @staticmethod
    def calculate(length: int, width=None):
        if width is None:
            return round(math.pi * length ** 2, 2)
        else:
            return length * width

    @staticmethod
    def calculate(*args: int) -> float:
        if len(args) == 1:
            return round(math.pi * args[0] ** 2, 2)
        else:
            return args[0] * args[1]
    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
