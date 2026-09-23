# Question No: 01

total_marks = 0
num_subjects = 5

print("Enter the marks for 5 subjects:")
for i in range(1, num_subjects + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    total_marks += marks

percentage = (total_marks / (num_subjects * 100)) * 100

if percentage >= 80:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

if percentage >= 40:
    status = "Pass"
else:
    status = "Fail"

print("\n--- Results ---")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Status: {status}")

# Question 2: Name details and string operations

name = input("Enter a student's name: ")

print("\n--- String Analysis ---")
print("Name in uppercase:", name.upper())
print("Name in lowercase:", name.lower())
print("Number of characters:", len(name))
print("First character:", name[0])
print("Last character:", name[-1])


# Question 3: Calculations on 10 numbers

numbers = []

print("Enter 10 numbers:")
for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    numbers.append(num)

total_sum = sum(numbers)
average = total_sum / len(numbers)
largest = max(numbers)
smallest = min(numbers)

even_count = 0
odd_count = 0

for num in numbers:
    
    if int(num) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\n--- Statistics ---")
print(f"Sum: {total_sum}")
print(f"Average: {average:.2f}")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")

# Question 4: Simple ATM Program

balance = 50000

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    
    if choice == "1":
        print(f"Your current balance is: ${balance}")
        
    elif choice == "2":
        deposit_amount = float(input("Enter amount to deposit: "))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"${deposit_amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")
            
    elif choice == "3":
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount > balance:
            print("Insufficient balance!")
        elif withdraw_amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            balance -= withdraw_amount
            print(f"${withdraw_amount} withdrawn successfully.")
            
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please select a valid menu option.")


# Question 5: Multiplication tables from 1 to n

n = int(input("Enter a number n: "))

print(f"\n--- Multiplication Tables from 1 to {n} ---")
for i in range(1, n + 1):
    print(f"\nTable of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
