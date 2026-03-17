from itertools import cycle

class to:
    @staticmethod
    def non_safe_array(data):
        if isinstance(data, list):
            if all(isinstance(x, int) for x in data):
                return data
            else:
                raise TypeError("List must contain only integers")
        elif isinstance(data, str):
            return [ord(char) for char in data]
        else:
            raise TypeError("Data must be string or list of integers")
    
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
        data = to.non_safe_array(data)
        data = [i + plus for i in data]
        return to.chars(data)
    
    @staticmethod
    def min (data, min):
        data = to.non_safe_array(data)
        data = [i - min for i in data]
        return to.chars(data)
    
    @staticmethod
    def mul (data, mul):
        data = to.non_safe_array(data)
        data = [i * mul for i in data]
        return to.chars(data)
    
    @staticmethod
    def div (data, div):
        if div == 0:
            raise ZeroDivisionError('Error! Division by zero!')
        data = to.non_safe_array(data)
        data = [i // div for i in data]
        return to.chars(data)

class armath:
    @staticmethod
    def sum (data, plus):
        data = to.non_safe_array(data)
        plus = to.non_safe_array(plus)
        r = [a + b for a, b in zip(data, cycle(plus))]
        return to.chars(r)
    
    @staticmethod
    def min (data, min):
        data = to.non_safe_array(data)
        min = to.non_safe_array(min)
        r = [a - b for a, b in zip(data, cycle(min))]
        return to.chars(r)
    
    @staticmethod
    def mul (data, mul):
        data = to.non_safe_array(data)
        mul = to.non_safe_array(mul)
        r = [a * b for a, b in zip(data, cycle(mul))]
        return to.chars(r)
    
    @staticmethod
    def div (data, div):
        data = to.non_safe_array(data)
        div = to.non_safe_array(div)
        if 0 in div:
            raise ZeroDivisionError('Error! Division by zero!')
        r = [a // b for a, b in zip(data, cycle(div))]
        return to.chars(r)

""" # Tests
print('to.array: ', to.array('Test')) 
print('to.chars: ', to.chars(to.array('Test')))
print('non_safe_array: ', to.chars(to.non_safe_array([65, 66, 67])), '\n')

print('nmath.sum: ', nmath.sum('Test', 5), '\tTest')
print('nmath.min: ', nmath.min('Test', 5), '\tTest')
print('nmath.mul: ', nmath.mul('Test', 5), '\tTest')
print('nmath.div: ', nmath.div('Test', 5), '\tTest')

print('armath.sum: ', armath.sum('Test', 'Check'), '\tTest\tCheck')
print('armath.min: ', armath.min('Test', 'Check'), '\tTest\tCheck')
print('armath.mul: ', armath.mul('Test', 'Check'), '\tTest\tCheck')
print('armath.div: ', armath.div('Test', 'Check'), '\tTest\tCheck')
""" # Tests