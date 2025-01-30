def main():
    print("Enter your booking:")
    print("1. premium economy")
    print("2. business class")
    print("3. economy class")
    print("4. first class")
    
    choice = int(input("Enter the choice of class: "))
    print("Which company flight you want to travel in?")
    print("1. Air India")
    print("2. Indigo")
    print("3. Air Vistara")
    airline_choice = int(input())
    print("Company of flight:")
    if airline_choice == 1:
        print("Air India")
    elif airline_choice == 2:
        print("Indigo")
    elif airline_choice == 3:
        print("Air Vistara")
    else:
        print("Invalid choice")
    seats = int(input("Enter number of seats: "))
    cost = 0
    if choice == 1:
        print("You selected premium economy")
        cost = 100000
    elif choice == 2:
        print("You selected business class")
        cost = 75000
    elif choice == 3:
        print("You selected economy class")
        cost = 50000
    elif choice == 4:
        print("You selected first class")
        cost = 150000
    else:
        print("You have not selected the correct class")
    total_cost = seats * cost
    maintenance_charges = 0.05 * total_cost
    net_cost = total_cost + maintenance_charges
    print(f"Cost: {cost}")
    print(f"Maintenance charges: {maintenance_charges}")
    print(f"Total flight price: {net_cost}")
if __name__ == "__main__":
    main()