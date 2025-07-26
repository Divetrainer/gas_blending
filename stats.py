def total_oxygen(requested_o2, tank_max_pressure):
    o2_normalized = float(requested_o2 / 100)
    o2_fill_to = ((o2_normalized - .21) / .79 ) * float(tank_max_pressure)
    return int(o2_fill_to)


def total_cuft(o2_added, tank_size):
    volume = (15 * tank_size) / o2_added
    return volume
