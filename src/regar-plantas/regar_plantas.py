def calculate_water_amount(plant_height, temperature):
    base_water = (plant_height / 10) * 50

    if temperature < 20:
        base_water *= 0.9
    elif temperature > 30:
        base_water *= 1.2

    base_water = max(10, min(base_water, 200))

    return round(base_water)

# Testes
assert calculate_water_amount(10, 25) == 50
assert calculate_water_amount(20, 15) == 90
assert calculate_water_amount(30, 35) == 180
assert calculate_water_amount(1, 5) == 10
assert calculate_water_amount(100, 50) == 200

print("✅ Todos os testes passaram!")
