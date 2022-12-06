import csv
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import integrate
from datetime import datetime
from statistics import mean
import math

#Importation du fichier CSV
fname = "Fichier_test_2.csv"
filepath=os.path.join("../dat/Raw/", fname)
data=pd.read_csv(filepath, sep=",",names=["date","Ax","Ay","Az"])

#conversion temps unix en human readable
data['date'] = pd.to_datetime(data['date'],unit='s')
data=data.set_index('date')

#initialisation parametres
#Fs=len(data)/(time.iloc[-1]-time.iloc[0]) #Calcul de la fréquence d'echantillonage du signal

data=data.resample('0.01S').mean() #resampling à 100Hz? (moyenne des valeurs sur 1/100s )
#on a bien 100 echantillons par seconde 

#Initialisation des variables temps et accélération
time=data.index
ax=data.iloc[:,0]
ay=data.iloc[:,1]
az=data.iloc[:,2]

#Calcul de la durée totale du signal 
t0 = time[0].second+ time[0].minute * 60+ time[0].hour * 3600
tf = time[len(data)-1].second+ time[len(data)-1].minute * 60+ time[len(data)-1].hour * 3600
time_tot = tf - t0

sub_data=np.array_split(data,4) # Partage de l'ensemble des données data (tableau) en 4 epochs (parts) de taille identique (en seconde a savoir)
# toto1=sp.integrate.simpson(sub_data[0]["Az"],dx=100) #Calcul de l'integrale sur la 1ere epoch Az.
# toto2=sp.integrate.simpson(sub_data[1]["Az"],dx=100)
# toto3=sp.integrate.simpson(sub_data[2]["Az"],dx=100)
# toto4=sp.integrate.simpson(sub_data[3]["Az"],dx=100)

#Calcul enmo 
enmo = np.sqrt(ax*ax + ay*ay + az*az) -1  # Calcul enmo -1 car on soustrait la gravité (1g) 
#enmo= enmo*9.81

#Calcul MAD
s = 0
n = len(data) #length of the time period
m = np.sqrt(ax*ax + ay*ay + az*az) #vector magnitude at each time point
moy_m = mean(m)
for i in range(0,n):
    s = abs(m - moy_m)+s
MAD = s/n


#nombre d epochs correspondant a 5 sec 
nb_epoch = time_tot/5.0
#Division de l'enmo en x epochs correspondant à 5sec 
epochs_enmo = np.array_split(enmo,nb_epoch) # Partage de la serie enmo en 12 epochs de taille identique (en seconde a savoir)
#Division du MAD en x epochs correspondant à 5sec 
epochs_MAD = np.array_split(MAD,nb_epoch)

#Calcul de la val moyenne de enmo et MAD sur chacune des epochs
enmo_moy = []
enmo_sum = []

for k in range(0, math.floor(nb_epoch)):
    print("k= ",k)
    somme = 0
    index = 0
    for lin in range(0, len(epochs_enmo[k]-1)): 
            index = index+1
            somme =epochs_enmo[k][lin] +somme
    enmo_sum.append(somme)
    moy = enmo_sum[k]/index    
    enmo_moy.append(moy)

MAD_moy = []
MAD_sum = []
for k in range(0, math.floor(nb_epoch)):
    print("k= ",k)
    somme = 0
    index = 0
    for lin in range(0, len(epochs_MAD[k]-1)): 
            index = index+1
            somme =epochs_MAD[k][lin] +somme
    MAD_sum.append(somme)
    moy = MAD_sum[k]/index    
    MAD_moy.append(moy)


# Application des seuils 

#calcul de la vitesse par integration de enmo
# integrales_enmo_list=[] #Liste des valeurs d'integrales des epoch d'enmo

# for i in epochs_enmo: #Calcul de l'intégrale de enmo sur chacune des epoch definies dans epochs_enmo
#     #print(i)
#     integrale_epoch_i=sp.integrate.simpson(i,dx=5) #Calcul de l'integrale sur l'epoch i
#     integrales_enmo_list.append(integrale_epoch_i) #ajout de la valeur de l'integrale pour l'epoch i a la liste des integrales


#Affichage des graphes
plt.figure(1)
plt.figure(figsize=(9, 3))

plt.subplot(411)
plt.plot(time, ax, '-b', lw=0.5, label ="x") #suivants mis en commentaires pour tester sur une donnée (ici x) sinon trop long à afficher
plt.title('Accelerations en fonction du temps')
plt.xlabel("temps en s")
plt.legend(['ax'],loc = 'upper right')

plt.subplot(412)
plt.plot(time, ay, '-r', lw=0.5, label ="y")
plt.xlabel("temps en s")
plt.legend(['ay'],loc = 'upper right')

plt.subplot(413)
plt.plot(time, az, '-c', lw=0.5, label ="z")
plt.xlabel("temps en s")
plt.legend(['az'],loc = 'upper right')

plt.subplot(414)
plt.plot(time, enmo, '-m', lw=0.5, label ="enmo")
plt.xlabel("temps en s")
plt.legend(['ENMO'],loc = 'upper right')



