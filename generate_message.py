from random import *

def generate_binary(length):
    return ''.join([str(randint(0, 1)) for _ in range(length)])

def generate_alphanumeric(length):
    lower = [chr(i+ord('a')) for i in range(26)]
    upper = [chr(i+ord('A')) for i in range(26)]
    digits = [str(i) for i in range(10)]
    alphanumeric = lower + upper + digits + [' ']
    return ''.join([alphanumeric[randint(0, len(alphanumeric)-1)] for _ in range(length)])

if __name__ == '__main__':
    print(generate_binary(100));
    print(generate_alphanumeric(100));
