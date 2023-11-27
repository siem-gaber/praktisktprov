#author : Siem GAber
#date : 2023-11-27

tal_input = input("Vilka tabeller vill du räkna?  ").split()
     
for val in tal_input:
   nummer = int(val)

   print("\n")
   for i in range(1, 11):
       Svar = nummer * i
       print(f"{nummer} * {i} = {Svar}")
   
   



50 


