from datetime import datetime

Dato_tid = []
Tid_start = []
Trykk_barometer = []
Trykkmaaler = []
Temperatur = []

fil = "/Users/tommy/Desktop/UiS Tommy/DAT120/-ving6/trykk_og_temperaturlogg_rune_time.csv.txt"

with open(fil, "r", encoding="UTF8") as fil:
    fil.readline()  
    
    for linje in fil:
       
        trykk_og_temperaturlogg = linje.strip().split(";")
        
        
        try:
            dato_tid = datetime.strptime(trykk_og_temperaturlogg[0], "%m.%d.%Y %H:%M")
            Dato_tid.append(dato_tid)  # Legg til som datetime-objekt
        except ValueError:
           
            continue

        # Legg inn de andre verdiene i lister
        Tid_start.append(trykk_og_temperaturlogg[1])
        Trykk_barometer.append(trykk_og_temperaturlogg[2])
        Trykkmaaler.append(trykk_og_temperaturlogg[3])
        Temperatur.append(trykk_og_temperaturlogg[4])


print("Dato_tid:", Dato_tid) 
print("Temperatur:", Temperatur)
print("Trykk_barometer", Trykk_barometer)
print("Trykkmaaler", Trykkmaaler)
print("Temperatur", Temperatur)

