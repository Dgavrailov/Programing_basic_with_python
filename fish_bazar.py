skumriq_price_per_kg = float(input())
caca_price_per_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

skumriq_final = skumriq_price_per_kg
caca_final = caca_price_per_kg
palamud_final = palamud_kg * (skumriq_price_per_kg + skumriq_price_per_kg * 0.6)
safrid_final = safrid_kg * (caca_price_per_kg + caca_price_per_kg * 0.8)
midi_final = midi_kg * 7.5

suma = (palamud_final + safrid_final + midi_final)
print(f'{suma:.2f}')
