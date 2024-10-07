import matplotlib.pyplot as plt
from datetime import datetime

fil1 = "temperatur_trykk_met_samme_rune_time_datasett.csv.txt"
fil2 = "trykk_og_temperaturlogg_rune_time.csv.txt"


tidspunkter1 = []
temperatur1 = []

tidspunkter2 = []
temperatur2 = []


with open(fil1, 'r', encoding='UTF8') as file:
    next(file)  
    for line in file:
        linje_split = line.split(";")
        if linje_split[2] and linje_split[3].strip():  
            tidspunkter1.append(linje_split[2])  
            temperatur1.append(linje_split[3])




with open(fil2, 'r', encoding='UTF8') as file:
    next(file)  
    for line in file:
        linje_split = line.split(";")
        if linje_split[0] and linje_split[4].strip():  
            tidspunkter2.append(linje_split[0]) 
            temperatur2.append(linje_split[4].strip("\n"))
            

datoer1 = [datetime.strptime(dato, '%d.%m.%Y %H:%M') for dato in tidspunkter1 if dato.strip()]
datoer2 = [datetime.strptime(dato, '%d.%m.%Y %H:%M') for dato in tidspunkter2 if dato.strip()]


plt.plot(datoer1, temperatur1, label='Fil 1', color='blue')  
plt.plot(datoer2, temperatur2, label='Fil 2', color='green')  


plt.title('Temperatur Plott fra Begge Filer')
plt.xlabel('Tid')
plt.ylabel('Temperatur (°C)')


plt.xticks(rotation=45)


plt.legend()


plt.tight_layout()
plt.show()
