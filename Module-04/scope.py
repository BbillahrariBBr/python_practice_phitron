balance = 580
def total_cost(price,quantity):
    global balance 
    cost = price*quantity
    balance = cost
    return cost

pay = total_cost(10,3)
print(balance)