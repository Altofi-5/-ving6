import matplotlib.pyplot as plt
from datetime import datetime


fil1 = "temperatur_trykk_met_samme_rune_time_datasett.csv.txt"
fil2 = "trykk_og_temperaturlogg_rune_time.csv.txt"


tidspunkter1 = []
temperatur1 = []
trykk1 = []  

tidspunkter2 = []
temperatur2 = []
trykk2 = [] 


format1 = "%d.%m.%Y %H:%M"  
format2 = "%m.%d.%Y %H:%M"  


# Leser inn data fra fil 1 (temperatur og trykk)
with open(fil1, "r", encoding="UTF8") as file:
    next(file)  # Hopper over overskriftslinjen
    for line in file:
        linje_split = line.split(";")
        if linje_split[2] and linje_split[3].strip() and linje_split[4].strip(): 
            try:
                tidspunkter1.append(datetime.strptime(linje_split[2], format1)) 
                temperatur1.append(float(linje_split[3].replace(",", "."))) 
                trykk1.append(float(linje_split[4].replace(",", "."))) 
            except ValueError:
                continue  # Hopper over linjer med ugyldig format


# Leser inn data fra fil 2 (temperatur og trykk)
with open(fil2, "r", encoding="UTF8") as file:
    next(file) 
    for line in file:
        linje_split = line.split(";")
        
        # Sjekker at linjen har nok kolonner før vi prøver å bruke dem
        if len(linje_split) > 5 and linje_split[0] and linje_split[4].strip() and linje_split[5].strip():  
            try:
                tidspunkter2.append(datetime.strptime(linje_split[0], format2)) 
                temperatur2.append(float(linje_split[4].strip("\n").replace(",", "."))) 
                trykk2.append(float(linje_split[5].strip("\n").replace(",", "."))) 
            except ValueError:
                continue  # Hopper over linjer med ugyldig format


# Plotter temperatur fra begge filer
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(tidspunkter1, temperatur1, label="Temperatur Fil 1", color="blue")
plt.plot(tidspunkter2, temperatur2, label="Temperatur Fil 2", color="green")
plt.title("Temperatur Plott fra Begge Filer")
plt.xlabel("Tid")
plt.ylabel("Temperatur (°C)")
plt.legend()

# Plotter atmosfærisk trykk fra begge filer
plt.subplot(2, 1, 2)
plt.plot(tidspunkter1, trykk1, label="Trykk Fil 1", color="red")
plt.plot(tidspunkter2, trykk2, label="Trykk Fil 2", color="orange")
plt.title("Atmosfærisk Trykk fra Begge Filer")
plt.xlabel("Tid")
plt.ylabel("Trykk (hPa)")
plt.legend()

plt.tight_layout()
plt.xticks(rotation=45)
plt.show()


