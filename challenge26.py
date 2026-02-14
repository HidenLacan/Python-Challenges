
'''
Statement of Exercise 26: 
Optimize spending at my favorite gas station. 

You have two options: 

- Individual gasoline: Costs 10 euros per fill-up. 
- Membership card: It costs 90 euros per year but every time you fill up 
The tank costs you 8.2 euros, you only pay 78% of the filling price. 

Each time you fill up the tank, you pay 78% of the price 
from the amount you paid for the last time until you reach a maximum discount 
50%. Accumulate the discount (0.78 ** 3). 

Create a function that, when passed to it, calculates the number of times I'm going to fill the tank, 
Tell me if it's worth buying the membership card or not. 

Examples: 
deboSerSocio(15); 

Returns: 
As a casual user, you get: 150
As a member, it costs you: 154.68487999999994 
It's not worth it for you to be a member. 
'''

def debo_ser_socio(times_filled:int) -> str:
    
    total_normal_cost = 10 * times_filled
    total_membership_cost = 0
    stop_discount = 0.5
    discount_partnership = 0.78 

    for t in range(1, times_filled +1):
        discount_calculated = discount_partnership ** t
        
        if discount_calculated >= stop_discount:
            total_membership_cost += 8.2 * discount_calculated
        else:
            total_membership_cost += 8.2 * stop_discount
        
        if total_membership_cost < total_normal_cost:
            message = "It's not worth it for you to be a member."
        else:
            message = "It's worth it for you to be a member."
            
    print(f"As a casual user, you get: {total_normal_cost}\n"
    f"As a member, it costs you: {total_membership_cost + 90}\n"
    f"{message}")
    
#debo_ser_socio(25)

def debo_ser_socio_refactor(times_filled:int) -> str:
    
    total_normal_cost = 10 * times_filled
    total_membership_cost = 0
    stop_discount = 0.5

    for t in range(1, times_filled +1):

        discount_calculated = 0.78 ** t
        general_discount = max(discount_calculated, stop_discount)
        total_membership_cost += 8.2 * general_discount
        
        message = ("It's not worth it for you to be a member." 
                   if total_membership_cost < total_normal_cost 
                   else "It's worth it for you to be a member."
                   )

    print(f"As a casual user, you get: {total_normal_cost}\n"
    f"As a member, it costs you: {total_membership_cost + 90}\n"
    f"{message}")
    
debo_ser_socio_refactor(15)