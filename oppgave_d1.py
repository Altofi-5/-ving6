

Navn = []
Stasjon = []
tidspunkter = []
temperatur = []
Lufttrykk = []


fil = "temperatur_trykk_met_samme_rune_time_datasett.csv.txt"

with open(fil, 'r', encoding='UTF8') as file:
    check=False
    for line in file:
        if check==True:
            linje_split=line.split(";")
            Navn.append(linje_split[0])
            Stasjon.append(linje_split[1])
            tidspunkter.append(linje_split[2])
            temperatur.append(linje_split[3])
            Lufttrykk.append(linje_split[4].strip("\n"))
        else:
            check=True
print("Navn:", Navn)
print("Stasjon:", Stasjon)            
print("Tidspunkter:", tidspunkter)
print("Temperaturer:", temperatur)
print("Lufttrykk:", Lufttrykk)
