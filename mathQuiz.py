import random
l = ["+", "-", "*", "/"]
m = 0
n = 0
def quiz(x, y, z):
    a = random.randrange(x, y+1)
    b = random.randrange(x, y+1)
    if z == "+":
        c = a + b
        answer(a, b, c, z)
    if z == "-":
        c = a - b
        answer(a, b, c, z)
    if z == "*":
        c = a * b
        answer(a, b, c, z)
    if z == "/":
        c = a / b
        if c == int(c):
            c = int(c)
        answer(a, b, c, z)
def answer(a, b, c, z):
    if str(c) == input(str(a) + " "+ z +" " + str(b) + " = "):
        print("Correct answer!")
        global n
        n += 1
    else:
        print("Incorrect answer. Correct answer is '" + str(c) + "'.")
        global m
        m += 1

print("Math Quiz")
print("The program ends when you get 5 questions wrong.")
while m != 5:
    k = random.randrange(0, 4)
    if k == 3:
        quiz(1, 10, l[k])
    elif k == 2:
        quiz(1, 10**random.randrange(1, 3), l[k])
    else:
        quiz(1, 10**random.randrange(1, 4), l[k])
print("\nCorrect answer: %d"%n)
print("Incorrect answer: %d"%m)