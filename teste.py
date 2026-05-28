list = ["m1", "m2", "m3", "m4", "m5"]
numero = 0
for x in range(len(list)):
    numero += 1
    print (f"{x} - {list[x]}")
    
while numero < len(list):
    print (f"{numero} - {list[numero]}")
    numero += 1