#author: Siem Gaber
#date: 2023-10-12
print("Ei22 - praktiskt prov ht23")

Rtot = int(input("Hur många resistorer har du ? "))

print("Ange resistorernas värden:")

resistorer = []
for i in range(Rtot):
    resistor = int(input(f"R{i + 1} = "))
    resistorer.append(resistor)

if any(val == 0 for val in resistorer):
    Serieresistans = 0
    Parallellresistans = 0
else:
    Serieresistans = sum(resistorer)
    Parallellresistans = 1 / sum(1 / val for val in resistorer)

print("Serieresistans:", Serieresistans)
print("Parallellresistans:", Parallellresistans)
