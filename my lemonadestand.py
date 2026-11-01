def great_customer():
    print("welcome to the lemonade stand!")
    print("fresh lemonade, made just for you")

great_customer()
price_per_cup = float(input("enter the price per cup in dollar"))
cup_solid = int(input("enter the number of cups sold: "))

def calculate_total(price, cups):
    total = price * cups
    return total

total_cost = calculate_total(price_per_cup, cup_solid)

rounded_total = round(total_cost, 2)
print("total cost:", rounded_total)
amount_paid = float(input("enter the amount paid by the customer: "))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)
print("change is : ", rounded_change)