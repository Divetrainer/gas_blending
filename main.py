from stats import total_oxygen, total_cuft, cost_per_cuft

class Tank:
    def __init__(self, size, max_pressure):
        self.size = size
        self.max_pressure = max_pressure

class Source_Tank:
    def __init__(self, size, max_pressure, cost, user_markup):
        self.size = size
        self.max_pressure = max_pressure
        self.cost = cost
        self.usercost = user_markup
    print("="*100)
    print("="*37+"DiveCenter Tank Information"+"="*36)
    print("="*100)
    print("for defaults please see Defaults.md")
    initalize = input("Would you like to change the default gas cost? ")
    if initalize.lower() == 'y' or initalize.lower() == 'yes':
        size = int(input("how many cuft is the source cylinder: "))
        max_pressure = int(input("what is the psi of this cylinder: "))
        cost = float(input("What was the total cost, in USD, for this fill: "))
        user_markup = float(input("what is the markup: "))
    else:
        max_pressure = 2400
        size = 120
        user_markup = 1.5
        
print()
print("="*100)
print("="*37+"Customer Tank Information"+"="*38)
print("="*100)
print()

Tank.size = input("What size tank are you filling(cuft): ")
Tank.max_pressure = input("What is the max working pressure(psi): ")

print("="*100)
print()

check = True
while check == True:
    print(f"Please make sure that your {Tank.size}cuft {Tank.max_pressure}psi tank is cleaned and properly drained")
    clean_check = input("Is it drained and cleaned(y/n): ")
    if clean_check.lower() == "n" or clean_check.lower() == "no":
        print("Please clean and drain the tank appropriately")
        print("Do not drain too fast, condensation will build, please drain no faster than 100psi a minute")
        print("="*100)
        check = True
    elif clean_check.lower() == "y" or clean_check.lower() == "yes":
        check = False
        print("="*100)
        break
    else:
        print("Please input a 'y' or 'yes' if the tank is cleaned or a 'n' or 'no' if it is empty.")
        print("="*100)
        check = True

print()
request = 0
while request < 21:
    request = int(input("What percent Oxygen is requested:"))
    if request < 21:
        print("Cannot create a lower than air O2 percentage, at this time. Please input a higher value")



o2_to_add = total_oxygen(request, Tank.max_pressure)

air_to_add = int(Tank.max_pressure) - o2_to_add
source_used = total_cuft(o2_to_add, Tank.max_pressure, Tank.size)


source_cost = cost_per_cuft(Source_Tank.size, Source_Tank.size) * source_used
customer_total = source_cost * Source_Tank.user_markup

source_used = "%.2f" % source_used
source_cost = "%.2f" % source_cost
customer_total = "%.2f" % customer_total


print()
print("*"*39+"GAS BLEND REQUIREMENTS"+"*"*39)
print(f"Add {o2_to_add} psi to the tank")
print(f"Add {air_to_add} psi of clean air to top off the mixture")
print(f"Once the tank has cooled, please validate O2 percent is {request}")
print("*"*100)
print()
print("*"*39+"GAS COST PRINTOUT"+"*"*44)
print(f"Total gas used is: {source_used} cuft")
#print(f"Total gas cost is: ${source_cost}")
print(f"Total Cost to the customer is: ${customer_total}")
print("*"*100)