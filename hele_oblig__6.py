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
                temperatur1.append(float(linje_split[3].replace(",",".")))  
            except ValueError:
                continue  


with open(fil2, "r", encoding="UTF8") as file:
    next(file)
    for line in file:
        linje_split = line.split(";")
        if linje_split[0] and linje_split[4].strip():  
            try:
                tidspunkter2.append(datetime.strptime(linje_split[0], format2))  
                temperatur2.append(float(linje_split[4].strip("\n").replace(",",".")))  
            except ValueError:
                continue  




fil3 = "trykk_og_temperaturlogg_rune_time.csv.txt" 

tidspunkter3 = []
temperatur3 = []


format3 = "%m.%d.%Y %H:%M"


with open(fil3, "r", encoding="UTF8") as file:
    next(file)  
    for line in file:
        linje_split = line.split(";")  
        if linje_split[0] and linje_split[4].strip():  
            try:
                tidspunkter3.append(datetime.strptime(linje_split[0], format3))
                temperatur3.append(float(linje_split[4].replace(",", ".")))  
            except ValueError:
                continue 


start_time = datetime(month=6, day=11, year=2021, hour=17, minute=31)
end_time = datetime(month=6, day=12, year=2021, hour=3, minute=5)


filtrert_tider = []
filtrert_temperaturer = []

for i in range(len(tidspunkter3)):
    if start_time <= tidspunkter3[i] <= end_time:
        filtrert_tider.append(tidspunkter3[i])
        filtrert_temperaturer.append(temperatur3[i])


if filtrert_tider == []:  
    print("Ingen data funnet i det gitte tidsvinduet.")
else:

    plt.plot(filtrert_tider, filtrert_temperaturer, color='purple', label='Temperature Fall')
    plt.title("Temperatur Fall Fra 11 til 12 Juni")
    plt.xlabel("Tid")
    plt.ylabel("Temperatur")
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()



fil4 = "temperatur_trykk_met_samme_rune_time_datasett.csv.txt"
fil5 = "trykk_og_temperaturlogg_rune_time.csv.txt"


tidspunkter4 = []
temperatur4 = []
trykk4 = []  

tidspunkter5 = []
temperatur5 = []
trykk5 = [] 
abstrykk5=[]

format4 = "%d.%m.%Y %H:%M"  
format5 = "%m.%d.%Y %H:%M"  


# Leser inn data fra fil 1 (temperatur_trykk)
with open(fil4, "r", encoding="UTF8") as file:
    next(file)  # Hopper over overskriftslinjen
    for line in file:
        linje_split = line.split(";")
        if linje_split[2] and linje_split[3].strip() and linje_split[4].strip(): 
            try:
                tidspunkter4.append(datetime.strptime(linje_split[2], format4)) 
                temperatur4.append(float(linje_split[3].replace(",", "."))) 
                trykk4.append(float(linje_split[4].replace(",", "."))) 
            except ValueError:
                continue  # Hopper over linjer med ugyldig format



with open(fil5, "r", encoding="UTF8") as file:
    next(file)
    for line in file:
        linje_split = line.split(";")
        if linje_split[0] and linje_split[2] and linje_split[3] and linje_split[4].strip():  
            try:
                tidspunkter5.append(datetime.strptime(linje_split[0], format5))  
                temperatur5.append(float(linje_split[4].strip("\n").replace(",",".")))
                trykk5.append(float(linje_split[2].strip("\n").replace(",", "."))*10)
                abstrykk5.append(float(linje_split[3].strip("\n").replace(",", "."))*10)
            except ValueError:
                continue  

plt.subplot(2, 1, 1)
plt.plot(tidspunkter4, temperatur4, label="Temperatur Fil 1", color="blue")
plt.plot(tidspunkter5, temperatur5, label="Temperatur Fil 2", color="green")
plt.plot(filtrert_tider, filtrert_temperaturer, color='purple', label='Temperatur Fall')
plt.title("Temperatur Plott fra Begge Filer")
plt.xlabel("Tid")
plt.ylabel("Temperatur (°C)")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(tidspunkter4, trykk4, label="Trykk Fil 5", color="green")
plt.plot(tidspunkter5, trykk5, label="Trykk Fil 5", color="orange")
plt.plot(tidspunkter5, abstrykk5, label="abstrykk Fil 5", color="blue")
plt.title("Trykk fra Begge Filer")
plt.xlabel("Tid")
plt.ylabel("Trykk")
plt.legend()

plt.tight_layout()

plt.show()



