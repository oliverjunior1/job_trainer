def water_temperature(temperature):
    if temperature >25:
        return 'Hot'
    elif temperature>=15<=25:
        return 'Warm'
    else:
        return 'cold'

print(water_temperature(26))