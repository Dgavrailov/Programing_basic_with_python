lenght = int(input())
width = int(input())
height = int(input())
percentage_non_free_volume = float(input())
fish_tank_volume_in_sm = lenght * width * height
total_volume_fish_tank_in_liters = fish_tank_volume_in_sm * 0.001 #защото от куб.см минаваме на куб.дм
percentage = percentage_non_free_volume * 0.01
needed_liters = total_volume_fish_tank_in_liters * (1 - percentage)
print(needed_liters)

