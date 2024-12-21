# X ~ Exp(1)
import random
import math

def exponencial(): 
    U = 1 - random.random()
    return -math.log(U)

def X(): 
    Y = exponencial()
    U = random.random()
    return U**(1/Y)

def sample(): 
    return [X() for _ in range(25)]

def main():
    print(sample())

if __name__ == '__main__':
    main()
    