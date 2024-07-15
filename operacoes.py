print(f"Enter two numbers separated by 'enter'") #o print com f é uma forma de fazer expressões com strings 
x = int(input())
y = int(input())

print("Select an option by typing the corresponding number and pressing 'enter':\n1. addition\n2. subtraction\n3. multiplication\n4. division")

def soma (a, b):
    return a+b
def subt (a, b):
    return a-b
def mult (a, b):
    return a*b
def divi (a, b):
    return (a/b)

c = int(input())

if c == 1:
    print(f"a + b = ", soma(x,y)) #as chaves fazem com que concatene string e inteiro
elif c == 2:
    print(f"a - b = ", subt(x,y))
elif c == 3:
    print(f"a * b = ", mult(x,y))
elif c == 4:
    print("a * b = ", divi(x,y))
else:
    print("Invalid option")
