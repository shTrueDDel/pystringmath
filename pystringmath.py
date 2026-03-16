from itertools import cycle

class to:
    @staticmethod
    def array (data):
        try:
            data = [ord(char) for char in data]
        except TypeError:
            raise TypeError('Data is not a string')
        return data
    
    @staticmethod
    def chars (data):
        try:
            data = ''.join(map(chr, data))
        except:
            raise TypeError('Data is not a correct')
        return data
    
class nmath:
    @staticmethod
    def sum (data, plus):
        data = to.array(data)
        data = [i + plus for i in data]
        return to.chars(data)
    
    @staticmethod
    def min (data, min):
        data = to.array(data)
        data = [i - min for i in data]
        return to.chars(data)
    
    @staticmethod
    def mul (data, mul):
        data = to.array(data)
        data = [i * mul for i in data]
        return to.chars(data)
    
    @staticmethod
    def div (data, div):
        if 0 in div:
            raise ZeroDivisionError('Error! Division by zero!')
        data = to.array(data)
        data = [i // div for i in data]
        return to.chars(data)

class armath:
    @staticmethod
    def sum (data, plus):
        data = to.array(data)
        plus = to.array(plus)
        r = [a + b for a, b in zip(data, cycle(plus))]
        return to.chars(r)
    
    @staticmethod
    def min (data, min):
        data = to.array(data)
        min = to.array(min)
        r = [a - b for a, b in zip(data, cycle(min))]
        return to.chars(r)
    
    @staticmethod
    def mul (data, mul):
        data = to.array(data)
        mul = to.array(mul)
        r = [a * b for a, b in zip(data, cycle(mul))]
        return to.chars(r)
    
    @staticmethod
    def div (data, div):
        if 0 in div:
            raise ZeroDivisionError('Error! Division by zero!')
        data = to.array(data)
        div = to.array(div)
        r = [a // b for a, b in zip(data, cycle(div))]
        return to.chars(r)

""" # Tests
print('to.array: ', to.array('Test')) 
print('to.chars: ', to.chars(to.array('Test')), '\n')

print('nmath.sum: ', nmath.sum('Test', 5), '\tTest')
print('nmath.min: ', nmath.min('Test', 5), '\tTest')
print('nmath.mul: ', nmath.mul('Test', 5), '\tTest')
print('nmath.div: ', nmath.div('Test', 5), '\tTest')

print('armath.sum: ', armath.sum('Test', 'Check'), '\tTest\tCheck')
print('armath.min: ', armath.min('Test', 'Check'), '\tTest\tCheck')
print('armath.mul: ', armath.mul('Test', 'Check'), '\tTest\tCheck')
print('armath.div: ', armath.div('Test', 'Check'), '\tTest\tCheck')
""" # Tests