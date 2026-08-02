# 
marksStudent = [12,14,16,17]
sum = 0
for mark in marksStudent:
    sum +=mark
    countSize = len(marksStudent)
average = sum / len(marksStudent)
print(f"sum of the mark is {sum}")
print(f"the average of the marks is {average}")
print(f"the size of the list is {countSize}")

products = []

while True:
    print("\n===== MENU =====")
    print("1. Add product")
    print("2. Remove product")
    print("3. Show products")
    print("4. Exit")

    choiceNumber = int(input("Enter your choice: "))

    if choiceNumber == 1:
        product = input("Enter the product name: ")
        products.append(product)
        print("Product added successfully.")

    elif choiceNumber == 2:
        product = input("Enter the product name to remove: ")

        if product in products:
            products.remove(product)
            print("Product removed successfully.")
        else:
            print("Product not found.")

    elif choiceNumber == 3:
        if len(products) == 0:
            print("No products available.")
        else:
            print("\nProducts:")
            for i, product in enumerate(products, start=1):
                print(f"{i}. {product}")

    elif choiceNumber == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
