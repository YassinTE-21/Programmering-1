from cgi import print_arguments
from secrets import choice

travelbag = []

while True:
   menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program\n")
   if menyval == "1":
       print (f"i väskan har du: ", end="")
       print(*travelbag, sep=",")
        
   elif menyval == "2":
       travelbag.append (input("Vad vill du lägga till?  "))

   elif menyval == "3":
    try:
        travelbag.remove (input("Vad vill du ta bort? "))

    except:
        input("Den här saken finns ej at ta bort. Tryck på Enter för att fortsätta. ")
        
   elif menyval == "4":
       break