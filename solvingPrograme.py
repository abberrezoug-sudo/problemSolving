inputNumber = int(input("Enter a number: "))
summ = 0

while not inputNumber == 0:
    summ += inputNumber
    countNumber += 1
    inputNumber = int(input("Enter another number (0 to exit): "))

print(f"the summe of the numbers is {summ}")
print(f"the count of the number is {countNumber}")