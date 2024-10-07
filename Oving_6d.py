Dato_tid = []
Tid_start = []
Trykk_barometer = []
Trykkmaaler = []
Temperatur = []

fil = "/Users/tommy/Desktop/UiS Tommy/DAT120/-ving6/trykk_og_temperaturlogg_rune_time.csv.txt"

with open(fil, "r", encoding="UTF8") as fil:
    fil.readline()  
    
    for linje in fil:
       
        check = True 
        
        if check == True:
            trykk_og_temperaturlogg = linje.strip().split(";")
           
            Dato_tid.append(trykk_og_temperaturlogg[0])
            Tid_start.append(trykk_og_temperaturlogg[1])  
            Trykk_barometer.append(trykk_og_temperaturlogg[2])
            Trykkmaaler.append(trykk_og_temperaturlogg[3])
            Temperatur.append(trykk_og_temperaturlogg[4])
            
         except ValueError:
            # Hopp over linjer med ugyldig datoformat (de som kommer etter 2/3)
            continue

# Sjekk at dataene er lagt til riktig
print("Dato_tid:", Dato_tid)  
print("Temperatur:", Temperatur) 


