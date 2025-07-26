from stats import total_oxygen, total_cuft

class Tank:
    def __init__(self, size, max_pressure):
        self.size = size
        self.max_pressure = max_pressure
    
Tank.size = input("What size tank are you using(cuft): ")
Tank.max_pressure = input("What is the max working pressure(psi): ")

print(f"Please make sure that your {Tank.size}cuft {Tank.max_pressure}psi tank is cleaned and properly drained")

check = True
while check == True:
    clean_check = input("Is it drained and cleaned(y/n): ")
    if clean_check.lower() == "n" or clean_check.lower() == "no":
        print("Please clean and drain the tank appropriately")
        print("Do not drain too fast, condensation will build, please drain no faster than 100psi a minute") 
        check = True
    elif clean_check.lower() == "y" or clean_check.lower() == "yes":
        check = False
        break
    else:
        print("Please input a 'y' or 'yes' if the tank is cleaned or a 'n' or 'no' if it is empty.")
        check = True

request = int(input("What percent Oxygen is requested:"))

o2_to_add = total_oxygen(request, Tank.max_pressure)

air_to_add = int(Tank.max_pressure) - o2_to_add

print("=========gas blend===========")
print(f"Add {o2_to_add} psi to the tank")
print(f"Add {air_to_add} psi of clean air to top off the mixture")
print(f"Once the tank has cooled, please validate O2 percent is {request}")
print("=============================")
