import math
from random import *
import matplotlib.pyplot as plt

class BinaryMessage:
    def __init__(self, value_nb, value_size = 8):
        self.value_nb = value_nb
        self.message = None
        self.value_size = value_size
        
    def get_message(self):
        return self.message

    def plot_values(self):
            values = [int(self.message[i*self.value_size:(i+1)*self.value_size], 2) for i in range(self.value_nb)]
            plt.plot(values)
            plt.show()



class RandomBinaryMessage(BinaryMessage):
    def __init__(self, value_nb):
        super().__init__(value_nb)
        self.generate_message()
    
    def generate_message(self):
        self.message = ''.join([str(randint(0, 1)) for _ in range(self.value_nb*self.value_size)])



class LinearBinaryMessage(BinaryMessage):
    def __init__(self, value_nb, mode_param = 2, max_error = 5):
        super().__init__(value_nb)
        self.mode_param = mode_param
        self.max_error = max_error
        self.value_size = math.ceil(math.log2(self.mode_param*self.value_nb+self.max_error))
        self.generate_message()

    def generate_message(self):
        values = [self.mode_param*i+randint(-self.max_error, self.max_error) for i in range(self.value_nb)]
        self.message = ''.join([bin(e)[2:].zfill(self.value_size) if e>=0 else '0'*self.value_size for e in values])



class AlphanumericMessage:
    def __init__(self, length, mode = 'random', value_size = 8, mode_param = None):
        self.length = length
        self.mode = mode
        self.message = None
        self.value_size = value_size
        self.mode_param = mode_param
        self.generate_message()

    def generate_message(self):
        lower = [chr(i+ord('a')) for i in range(26)]
        upper = [chr(i+ord('A')) for i in range(26)]
        digits = [str(i) for i in range(10)]
        alphanumeric = lower + upper + digits + [' ']
        self.message = ''.join([alphanumeric[randint(0, len(alphanumeric)-1)] for _ in range(self.length)])

    def get_message(self):
        return self.message



if __name__ == '__main__':
    m = LinearBinaryMessage(1000, max_error=50)
    m.plot_values()