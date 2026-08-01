
# ==========================================
# Python Basic Programs
# ==========================================
# This file contains three basic Python programs:
# 1. Multiplication Table
# 2. Bank Account Management System
# 3. Student Grades Calculator
#
# Purpose:
# Practice Python fundamentals including:
# - Variables
# - User Input
# - Conditional Statements
# - Loops
# - Functions
# - Menu-Driven Programs
# ==========================================


# ------------------------------------------
# Program 1: Multiplication Table
# ------------------------------------------
def multiplication_table():
    print("\n===== Multiplication Table =====")

    number = int(input("Enter a number: "))

    print(f"\nMultiplication Table of {number}\n")

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

    print()


# ------------------------------------------
# Program 2: Bank Account Management System
# ------------------------------------------
def bank_system():
    print("\n===== Bank Account Management =====")

    client_name = input("Enter your name: ")
    balance = 0

    while True:
        print("\nWelcome,", client_name)
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Deposit successful.")
            else:
                print("Invalid amount.")

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")

        elif choice == "3":
            print(f"Current Balance: {balance:.2f}")

        elif choice == "4":
            print("Thank you for using our bank system.")
            break

        else:
            print("Invalid choice.")


# ------------------------------------------
# Program 3: Student Grades Calculator
# ------------------------------------------
def student_grades():
    print("\n===== Student Grades Calculator =====")

    student_name = input("Enter student name: ")

    grade1 = float(input("Enter Grade 1: "))
    grade2 = float(input("Enter Grade 2: "))
    grade3 = float(input("Enter Grade 3: "))

    average = (grade1 + grade2 + grade3) / 3

    print("\nStudent:", student_name)
    print("Average:", round(average, 2))

    if average >= 16:
        print("Mention: Excellent")
    elif average >= 14:
        print("Mention: Very Good")
    elif average >= 12:
        print("Mention: Good")
    elif average >= 10:
        print("Mention: Pass")
    else:
        print("Mention: Fail")


# ------------------------------------------
# Main Menu
# ------------------------------------------
def main():
    while True:
        print("\n===================================")
        print("      PYTHON BASIC PROGRAMS")
        print("===================================")
        print("1. Multiplication Table")
        print("2. Bank Account Management")
        print("3. Student Grades Calculator")
        print("4. Exit")

        choice = input("Select a program: ")

        if choice == "1":
            multiplication_table()

        elif choice == "2":
            bank_system()

        elif choice == "3":
            student_grades()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# ------------------------------------------
# Start Program
# ------------------------------------------
main()