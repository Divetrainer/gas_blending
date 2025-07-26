def total_oxygen(requested_o2, tank_max_pressure):
    o2_normalized = float(requested_o2 / 100)
    o2_fill_to = ((o2_normalized - .21) / .79 ) * float(tank_max_pressure)
    return int(o2_fill_to)


def total_cuft(o2_added, tank_max_pressure, tank_size):
    if int(o2_added) == 0:
        o2_added = 1
    volume = (int(o2_added) / int(tank_max_pressure)) * int(tank_size)
    return volume

def cost_per_cuft(cuft_total, total_cost):
    cost_cuft = total_cost / cuft_total
    return cost_cuft

def max_operating_depth(request):
    o2_normalized = float(request/100)
    max_depth = 33 * ((1.4/(o2_normalized)) - 1 )
    return int(max_depth)

def contingency_max(request):
    o2_normalized = float(request/100)
    cont_depth = 33 * ((1.6/(o2_normalized)) - 1 )
    return int(cont_depth)