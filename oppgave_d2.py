
Navn = []
tid_siden_start = []
tidspunkter = []
temperatur = []
trykk = []

fil = "trykk_og_temperaturlogg_rune_time.csv.txt"

with open(fil, 'r', encoding='UTF8') as file:
    check=False
    for line in file:
        if check==True:
            linje_split=line.split(";")
            tidspunkter.append(linje_split[0])
            tid_siden_start.append(linje_split[1])
            trykk.append(linje_split[3])
            temperatur.append(linje_split[4].strip("\n"))
        else:
            check=True
print("Tidspunkter:", tidspunkter)
print("Tid siden start:", tid_siden_start)
print("Trykk:", trykk)
print("Temperaturer:", temperatur)