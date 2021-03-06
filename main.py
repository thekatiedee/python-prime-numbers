#INSTRUCTIONS: Write a program that displays the first 50 prime numbers in descending order. Use a stack to store prime numbers.
# Stack Class

class Stack:
    def __init__(self):
        self.__elements = []

    # Return true if the stack is empty
    def isEmpty(self):
        return len(self.__elements) == 0

    # Returns the element at the top of the stack
    # without removing it from the stack.
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(self.__elements) - 1]

    # Stores an element into the top of the stack
    def push(self, value):
        self.__elements.append(value)

    # Removes the element at the top of the stack and returns it
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop()

    # Return the size of the stack
    def getSize(self):
        return len(self.__elements)

def isItPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def getPrime():
    i = 1
    myPrimes = Stack()
    count = 0
    while True:
        i += 1
        if isItPrime(i) == True:
            count += 1
            myPrimes.push(i)
            if count == 50:
                break
        else:
            pass
    print('These are the first 50 prime numbers in descending order:')
    for i in range(50):
        reversalStack = myPrimes.pop()
        print(reversalStack)

def main():
    getPrime()

main()
