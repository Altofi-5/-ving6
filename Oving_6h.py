import matplotlib.pyplot as plt
from datetime import datetime

# Filnavnene
fil1 = "temperatur_trykk_met_samme_rune_time_datasett.csv.txt"


# Lister for tidspunkter, temperaturer og trykk fra begge filer
tidspunkter1 = []
temperatur1 = []
trykk1 = []




format1 = "%d.%m.%Y %H:%M"


# Data fra fil 1 (temperatur og trykk)
with open(fil1, "r", encoding="UTF8") as file:
    next(file)  
    for line in file:
        linje_split = line.split(";")
        if len(linje_split) > 4 and linje_split[2] and linje_split[3].strip() and linje_split[4].strip():
            try:
                tidspunkter1.append(datetime.strptime(linje_split[2], format1)) 
                temperatur1.append(float(linje_split[3].replace(",", ".")))  
                trykk1.append(float(linje_split[4].replace(",", "."))) 
            except ValueError:
                continue 



# Funksjon for å finne gjennomsnitt
def glidende_gjennomsnitt(tider, temperaturer, n):
    gyldige_tidspunkter = []
    gjennomsnittstemperaturer = []
    
    for i in range(n, len(temperaturer) - n):
        gjennomsnitt = sum(temperaturer[i-n:i+n+1]) / (2 * n + 1)
        gjennomsnittstemperaturer.append(gjennomsnitt)
        gyldige_tidspunkter.append(tider[i])
    
    return gyldige_tidspunkter, gjennomsnittstemperaturer

# Beregn gjennomsnitt for temperatur fra fil 1 med n=30
n = 30
gj_tidspunkter1, gj_temperaturer1 = glidende_gjennomsnitt(tidspunkter1, temperatur1, n)


plt.figure(figsize=(10, 8))


plt.subplot(2, 1, 1)
plt.plot(tidspunkter1, temperatur1, label="Temperatur Fil 1", color="blue")
plt.plot(gj_tidspunkter1, gj_temperaturer1, label="Glidende Gjennomsnitt Fil 1 (n=30)", color="orange")
plt.title("Temperatur Plott")
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.legend()


plt.subplot(2, 1, 2)
plt.plot(tidspunkter1, trykk1, label="Trykk Fil 1", color="red")
plt.title("Atmosfærisk Trykk")
plt.xlabel("Tid")
plt.ylabel("Trykk")
plt.legend()


plt.tight_layout()
plt.xticks(rotation=45)
plt.show()
