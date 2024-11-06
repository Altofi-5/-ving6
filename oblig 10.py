# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:59:46 2024

@author: BMSst
"""
import datetime
import pandas as pd

# Les filene
df1_fil = ('temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt')
df2_fil = ('trykk_og_temperaturlogg_rune_time.csv.txt')
df3_fil = ('temperatur_trykk_met_samme_rune_time_datasett.csv.txt')



def fil_spliter(df2_fil):
    try:
        with open (df2_fil, "r", encoding= "UTF-8") as fil1:
            
            first_line = fil1.readline()
            fil_linjer = fil1.readlines()
            for linje, linje in enumerate(fil_linjer, start=1):
                linje = linje.strip()
                deler = linje.split(";")
                
                datotider1 = deler[0]
                datotid = dato_tid(datotider1)
                
                try:
                    tempraturer = deler[4]
                    temp = float(tempraturer.replace(',', '.'))
                    trykkk= deler[3]
                    trykk = float(trykkk.replace(',','.'))
                except Exception:
                    print("Rito")
                yield datotid, temp, trykk
                
                

    except FileNotFoundError:
        print(f" Filen {df2_fil} ble ikke funnet.")
        
        
        
r_dt = []

r_temp = []

r_trykk = []

def dato_tid(dato):
    try: 
        dt = datetime.datetime.strptime(dato, '%m.%d.%Y %H:%M')
        return dt
    except Exception:
        print("tidspunket her INTE RITOOOO!", dato)
    
#
#"temperatur_trykk_met_samme_rune_time_datasett.csv.txt"
for datotid, temp, trykk in fil_spliter(df2_fil):
    r_dt.append(datotid)
    r_temp.append(temp)
    r_trykk.append(trykk)
    

print (f" Datoer: {r_dt}")
print (f"Datoer: {r_temp}")

###############################################################################

def fil_spliter2(df3_fil):
    try:
        with open (df3_fil, "r", encoding= "UTF-8") as fil2:
            
            first_line2 = fil2.readline()
            fil_linjer2 = fil2.readlines()
            for linje2, linje2 in enumerate(fil_linjer2, start=1):
                linje2 = linje2.strip()
                deler2 = linje2.split(";")
                
                datotider2 = deler2[2]
                datotid2 = dato_tid2(datotider2)
                
                try:
                    tempraturer2 = deler2[3]
                    temp2 = float(tempraturer2.replace(',','.'))
                    trykkk2 = deler2[4]
                    trykk2 = float(trykkk2.replace(',','.'))
                except Exception:
                    print("Rito")
                yield datotid2, temp2, trykk2
                
                

    except FileNotFoundError:
        print(f" Filen {df3_fil} ble ikke funnet.")
        
        
        
r_dt2 = []

r_temp2 = []

r_trykk2 = []

def dato_tid2(dato2):
    try: 
        dt = datetime.datetime.strptime(dato2, '%d.%m.%Y %H:%M')
        return dt
    except Exception:
        print("neo gikk feil", dato2)
    

for datotid2, temp2, trykk2 in fil_spliter2(df3_fil):
    r_dt2.append(datotid2)
    r_temp2.append(temp2)
    r_trykk2.append(trykk2)
    

print (f" Datoer: {r_dt2}")
print (f"Datoer: {r_temp2}")







#######################################################################################################################


import matplotlib.pyplot as plt

#######################################################################################################################
# oppgave A

# Kombinerer tidspunktene og temperaturene fra begge datasettene i pandas DataFrame
df1 = pd.DataFrame({'time': r_dt, 'temp': r_temp})
df2 = pd.DataFrame({'time': r_dt2, 'temp': r_temp2})

# Slå sammen de to datasettene på tidspunktene som er felles
common_times = pd.merge(df1, df2, on='time', how='inner')

# Plot temperaturene
plt.plot(common_times['time'], common_times['temp_x'], label='Sola Temperatur')  # 'temp_x' er for df1
plt.plot(common_times['time'], common_times['temp_y'], label='Meteorologisk Temperatur')  # 'temp_y' er for df2

plt.xlabel('Tid')
plt.ylabel('Temperatur (°C)')
plt.legend()
plt.xticks(rotation=45)
plt.title('Temperaturfall for begge datasettene')
plt.show()


#######################################################################################################################
# oppgave B


# Kombinerer temperaturene fra begge datasettene i ett plot
plt.hist(r_temp, bins=range(int(min(r_temp)), int(max(r_temp)) + 2), edgecolor='black', alpha=0.5, label='Sola Temperatur')
plt.hist(r_temp2, bins=range(int(min(r_temp2)), int(max(r_temp2)) + 2), edgecolor='black', alpha=0.5, label='Meteorologisk Temperatur')

plt.xlabel('Temperatur (°C)')
plt.ylabel('Antall målinger')
plt.legend()
plt.title('Histogram over temperaturer')
plt.show()

#######################################################################################################################
# oppgave c


# Kombinerer dataene i en DataFrame
df1 = pd.DataFrame({'time': r_dt, 'temp': r_temp, 'trykk': r_trykk})
df2 = pd.DataFrame({'time': r_dt2, 'temp': r_temp2, 'trykk': r_trykk2})

# Merge de to datasettene basert på felles tidspunkter
common_times = pd.merge(df1, df2, on='time', how='inner')

# Beregn differansen mellom absolutt trykk og barometrisk trykk
common_times['differanse'] = common_times['trykk_x'].astype(float) - common_times['trykk_y'].astype(float)

#Etter at dataene er lastet inn i to separate DataFrames (df1 og df2), merges de sammen basert på felles tidspunkter (time).
#Differansen mellom de to trykkene (trykk_x og trykk_y) beregnes, og lagres i en ny kolonne differanse.

# Glatt differansen med et glidende gjennomsnitt for 10 forrige og 10 neste elementer
common_times['glattet_differanse'] = common_times['differanse'].rolling(window=21, min_periods=1).mean()

# Plott differansen og den glatte gjennomsnittet
plt.figure(figsize=(10, 6))
plt.plot(common_times['time'], common_times['differanse'], label='Differanse mellom trykk', alpha=0.6)
plt.plot(common_times['time'], common_times['glattet_differanse'], label='Glattet differanse', linewidth=2)
plt.xlabel('Tid')
plt.ylabel('Trykkdifferanse (hPa)')
plt.legend()
plt.title('Differanse mellom Absolutt og Barometrisk Trykk')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


######################################################################################################################
# oppgave d



df1_fil = ('temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt')

# Funksjon for å splitte dataene (Sinnes og Sauda)
def fil_spliter_3(df1_fil):
    try:
        with open(df1_fil, "r", encoding="UTF-8") as fil3:
            first_line = fil3.readline()
            fil3_linjer = fil3.readlines()
            for linje3 in fil3_linjer:
                linje3 = linje3.strip()
                deler3 = linje3.split(";")
                
                datotider3 = deler3[2]
                datotid3 = dato_tid2(datotider3)
                
                
                try:
                    temp3 = float(deler3[3].replace(',', '.'))
                    trykk3 = float(deler3[4].replace(',', '.'))
                    station3 = deler3[0].split("_")[0]  # Ex: Sinnes or Sauda based on filename
                except Exception:
                    continue
                yield datotid3, temp3, trykk3, station3
    except FileNotFoundError:
        print(f"Filen {df1_fil} ble ikke funnet.")

def dato_tid2(dato3):
    try: 
        dt = datetime.datetime.strptime(dato3, '%d.%m.%Y %H:%M')
        return dt
    except Exception:
        print("tidspunket her INTE RITOOOO!", dato3)



# Plotte dataene fra alle værstasjonene
r_dt_sinnes = []
r_temp_sinnes = []
r_trykk_sinnes = []

# Hent data fra Sinnes og Sauda
for datotid3, temp3, trykk3, station3 in fil_spliter_3('temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt'):
    if station3 == "Sirdal - Sinnes":
        r_dt_sinnes.append(datotid3)
        r_temp_sinnes.append(temp3)
        r_trykk_sinnes.append(trykk3)

#########################################################################################################

# Funksjon for å splitte dataene (Sinnes og Sauda)
def fil_spliter_4(df1_fil):
    try:
        with open(df1_fil, "r", encoding="UTF-8") as fil4:
            first_line = fil4.readline()
            fil4_linjer = fil4.readlines()
            for linje4 in fil4_linjer:
                linje4 = linje4.strip()
                deler4 = linje4.split(";")
                
                datotider4 = deler4[2]
                datotid4 = dato_tid4(datotider4)
                
                
                try:
                    temp4 = float(deler4[3].replace(',', '.'))
                    trykk4 = float(deler4[4].replace(',', '.'))
                    station4 = deler4[0].split("_")[0]  # Ex: Sinnes or Sauda based on filename
                except Exception:
                    continue
                yield datotid4, temp4, trykk4, station4
    except FileNotFoundError:
        print(f"Filen {df1_fil} ble ikke funnet.")

def dato_tid4(dato4):
    try: 
        dt = datetime.datetime.strptime(dato4, '%d.%m.%Y %H:%M')
        return dt
    except Exception:
        print("tidspunket her INTE RITOOOO!", dato4)



# Plotte dataene fra alle værstasjonene
r_dt_sauda = []
r_temp_sauda = []
r_trykk_sauda = []

# Hent data fra Sinnes og Sauda
for datotid4, temp4, trykk4, station3 in fil_spliter_4('temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt'):
    if station3 == "Sauda":
        r_dt_sauda.append(datotid4)
        r_temp_sauda.append(temp4)
        r_trykk_sauda.append(trykk4)

# Sola data
plt.plot(r_dt, r_temp, label='Sola Temperatur', color='blue', linestyle='-', marker='o')
# Meteorologisk Institutt data
plt.plot(r_dt2, r_temp2, label='Meteorologisk Temperatur', color='green', linestyle='-', marker='x')
# Sinnes data
plt.plot(r_dt_sinnes, r_temp_sinnes, label='Sinnes Temperatur', color='red', linestyle='-', marker='^')
# Sauda data
plt.plot(r_dt_sauda, r_temp_sauda, label='Sauda Temperatur', color='purple', linestyle='-', marker='s')

# Tittel og aksebeskrivelser
plt.title('Temperaturdata for Sola, Sauda og Sinnes')
plt.xlabel('Tid')
plt.ylabel('Temperatur (°C)')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()







