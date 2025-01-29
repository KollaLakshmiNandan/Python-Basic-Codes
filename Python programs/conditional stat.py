def movie_ticket():
    age = int(input("\nEnter your age: "))
    if age < 5:
        print("Free Entry!")
    elif 5 <= age <= 12:
        print("Child Ticket: $5")
    elif 13 <= age <= 18:
        print("Teen Ticket: $8")
    elif 19 <= age <= 60:
        print("Adult Ticket: $12")
    else:
        print("Senior Citizen Discount: $6")

def login_system():
    stored_password = "Secure@123"
    user_password = input("\nEnter your password: ")
    if user_password == stored_password:
        print("Login Successful!")
    else:
        print("Incorrect Password! Try Again.")

def grade_calculator():
    marks = int(input("\nEnter your marks: "))
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F (Failed)")

def traffic_light():
    light = input("\nEnter traffic light color (Red, Yellow, Green): ").lower()
    if light == "red":
        print("Stop!")
    elif light == "yellow":
        print("Slow Down!")
    elif light == "green":
        print("Go!")
    else:
        print("Invalid Input! Please enter Red, Yellow, or Green.")

def banking_system():
    balance = 5000  
    withdraw_amount = int(input("\nEnter withdrawal amount: "))
    if withdraw_amount > balance:
        print("Insufficient Balance!")
    elif withdraw_amount <= 0:
        print("Invalid Amount! Enter a valid withdrawal amount.")
    else:
        balance -= withdraw_amount
        print(f"Withdrawal Successful! Remaining Balance: ${balance}")

def even_odd_checker():
    num = int(input("\nEnter a number: "))
    if num % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")

def job_eligibility():
    age = int(input("\nEnter your age: "))
    experience = int(input("Enter years of experience: "))
    if age >= 18 and experience >= 2:
        print("Eligible for the job!")
    else:
        print("Not eligible for the job.")

def main():
    while True:
        print("\nConditional Statements - Multi-Feature System")
        print("1. Movie Ticket Pricing")
        print("2. Login System")
        print("3. Grade Calculator")
        print("4. Traffic Light System")
        print("5. Banking System (Withdrawal Check)")
        print("6. Even or Odd Number Checker")
        print("7. Job Eligibility Check")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            movie_ticket()
        elif choice == '2':
            login_system()
        elif choice == '3':
            grade_calculator()
        elif choice == '4':
            traffic_light()
        elif choice == '5':
            banking_system()
        elif choice == '6':
            even_odd_checker()
        elif choice == '7':
            job_eligibility()
        elif choice == '8':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
