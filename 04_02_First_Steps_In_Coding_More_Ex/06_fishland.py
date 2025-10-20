skumriq_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = float(input())

palamud_price = skumriq_price + skumriq_price * 0.60
safrid_price = caca_price + caca_price * 0.80
midi_price = 7.50

final_price = palamud_kg * palamud_price + safrid_kg * safrid_price + midi_kg * midi_price

print(f'{final_price:.2f}')
