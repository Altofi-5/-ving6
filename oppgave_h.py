from datetime import datetime
import matplotlib.pyplot as plt

file_path = "trykk_og_temperaturlogg_rune_time.csv.txt" 

tidspunkter1 = []
temperatur1 = []


format1 = "%m.%d.%Y %H:%M"


with open(file_path, 'r') as file:
    next(file)  
    for line in file:
        linje_split = line.split(";")  
        if linje_split[0] and linje_split[4].strip():  
            try:
                tidspunkter1.append(datetime.strptime(linje_split[0], format1))
                temperatur1.append(float(linje_split[4].replace(",", ".")))  
            except ValueError:
                continue 


start_time = datetime(month=6, day=11, year=2021, hour=17, minute=31)
end_time = datetime(month=6, day=12, year=2021, hour=3, minute=5)


filtered_times = []
filtered_temperatures = []

for i in range(len(tidspunkter1)):
    if start_time <= tidspunkter1[i] <= end_time:
        filtered_times.append(tidspunkter1[i])
        filtered_temperatures.append(temperatur1[i])


if filtered_times == []:  
    print("Ingen data funnet i det gitte tidsvinduet.")
else:

  
    plt.plot(filtered_times, filtered_temperatures, color='purple', label='Temperature Fall')
    plt.title("Temperatur Fall Fra 11 til 12 Juni")
    plt.xlabel("Tid")
    plt.ylabel("Temperatur")
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()
