import matplotlib.pyplot as plt
from datetime import datetime


fil1 = "temperatur_trykk_met_samme_rune_time_datasett.csv.txt"
fil2 = "trykk_og_temperaturlogg_rune_time.csv.txt"


tidspunkter1 = []
temperatur1 = []

tidspunkter2 = []
temperatur2 = []


format1 = "%d.%m.%Y %H:%M"  
format2 = "%m.%d.%Y %H:%M"  


with open(fil1, "r", encoding="UTF8") as file:
    next(file)  
    for line in file:
        linje_split = line.split(";")
        if linje_split[2] and linje_split[3].strip():  
            try:
                tidspunkter1.append(datetime.strptime(linje_split[2], format1))  
                temperatur1.append(linje_split[3])  
            except ValueError:
                continue  


with open(fil2, "r", encoding="UTF8") as file:
    next(file)  
    for line in file:
        linje_split = line.split(";")
        if linje_split[0] and linje_split[4].strip():  
            try:
                tidspunkter2.append(datetime.strptime(linje_split[0], format2))  
                temperatur2.append(linje_split[4].strip("\n"))  
            except ValueError:
                continue  


plt.plot(tidspunkter1, temperatur1, label="Fil 1", color="blue")
plt.plot(tidspunkter2, temperatur2, label="Fil 2", color="green")

plt.title("Temperatur Plott fra Begge Filer")
plt.xlabel("Tid")
plt.ylabel("Temperatur")


plt.show()
