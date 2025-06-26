# addition
num1 = [4, 7, 8]
num2 = [9, 5, 6]

add = map(lambda x, y: x + y, num1, num2)
print("The addition of both lists results in:")
print(list(add))

# squaring
numlist = [1, 2, 3]
def sq(n):
    return n*n

squaring = list(map(sq, numlist))
print("The square of the numbers in the list:")
print(squaring)