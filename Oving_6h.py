import matplotlib.pyplot as plt
from datetime import datetime

fil1 = "temperatur_trykk_met_samme_rune_time_datasett.csv.txt"


tidspunkter1, temperatur1 = [], []
format1 = "%d.%m.%Y %H:%M" 

# Data fra filen
with open(fil1, "r", encoding="UTF8") as file:
    next(file)  
    for line in file:
        linje_split = line.split(";")
        if len(linje_split) > 4:  # Sjekker at linjen har nok elementer
            try:
                tidspunkter1.append(datetime.strptime(linje_split[2], format1)) 
                temperatur1.append(float(linje_split[3].replace(",", "."))) 
            except ValueError:
                continue  # Hopp over linjer med ugyldig format


start_tid = datetime.strptime("11.06.2021 17:31", format1)
slutt_tid = datetime.strptime("12.06.2021 03:05", format1)


start_index = next(i for i, t in enumerate(tidspunkter1) if t >= start_tid)
slutt_index = next(i for i, t in enumerate(tidspunkter1) if t >= slutt_tid)


utvalgte_tidspunkter = tidspunkter1[start_index:slutt_index + 1]
utvalgte_temperaturer = temperatur1[start_index:slutt_index + 1]


plt.figure(figsize=(10, 5))
plt.plot(utvalgte_tidspunkter, utvalgte_temperaturer, label="Temperaturfall (11. juni - 12. juni)", color="purple")
plt.title("Temperaturfall fra 11. juni 2021 kl. 17:31 til 12. juni 2021 kl. 03:05")
plt.xlabel("Tid")
plt.ylabel("Temperatur (°C)")
plt.xticks(rotation=45)
plt.legend()


plt.tight_layout()
plt.show()
