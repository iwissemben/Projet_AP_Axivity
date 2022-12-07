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
fname = "Resampled_10Hz_Wissem_rando.csv"
filepath=os.path.join("../dat/Converted/", fname)
data=pd.read_csv(filepath, sep=",")

#conversion temps unix en human readable
data['date'] = pd.to_datetime(data['date'])
data=data.set_index('date')

#initialisation parametres
#Fs=len(data)/(time.iloc[-1]-time.iloc[0]) #Calcul de la fréquence d'echantillonage du signal

#Initialisation des variables temps et accélération
time=data.index
ax=data.iloc[:,0]
ay=data.iloc[:,1]
az=data.iloc[:,2]

#Calcul de la durée totale du signal 
t0 = time[0].second+ time[0].minute * 60+ time[0].hour * 3600
tf = time[len(data)-1].second+ time[len(data)-1].minute * 60+ time[len(data)-1].hour * 3600
time_tot = tf - t0


#Calcul du nombre d'epochs possible correspondant a des periodes de 5 sec pour partager le signal
nb_epoch = time_tot/30

#Calcul enmo sur l'ensemble du signal en chaque instant puis le converti en ENMONZ
enmo = np.sqrt(ax*ax + ay*ay + az*az) -1  # Calcul enmo -1 car on soustrait la gravité (1g) 
enmo[enmo<0]=0 #ramene les valeurs negatives à 0 (ENMONZ)


# #Calcul MAD sur l'ensemble data
# s = 0
# n = len(data) #length of the time period
# m = np.sqrt(ax*ax + ay*ay + az*az) #vector magnitude at each time point sur l'ensemble du signal
# moy_m = mean(m) #moyenne de l'amplitude du vecteur acceleration de l'ensemble du signal


# for i in range(0,n):
#     abs(m - moy_m)
#     s = abs(m - moy_m)+s #Vecteur S ensemble du signal
# MAD = s/n #Valeur unique sur l'ensemble du signal

data["ENMONZ"]=enmo #ajout du vecteur des enmo comme colonne au dataframe
# data["MAD"]=MAD   #ajout du vecteur des enmo comme colonne au dataframe


# Partage du dataframe comportant les données data en un nombre d'epochs (parts) de taille identique (de 5s)
sub_data=np.array_split(data,nb_epoch) 


# toto1=sp.integrate.simpson(sub_data[0]["Az"],dx=100) #Calcul de l'integrale sur la 1ere epoch Az.

#Calcul des valeus moyennes de enmo et MAD sur chacune des epochs
for i in range(len(sub_data)):
    sub_data[i]["Moy_ENMONZ"]=mean(sub_data[i]["ENMONZ"])
    #Lsub_data[i]["Moy_MAD"]=mean(sub_data[i]["MAD"])

# Application des seuils et reconaissance de l'activité

#Pour chaque epoch
for i in range(len(sub_data)):
    if 0 <= sub_data[i]["Moy_ENMONZ"][1] <= 0.032:
        sub_data[i]["Activity_type"]="Sedentary_PA"
    if 0.032 <sub_data[i]["Moy_ENMONZ"][1] <= 0.173:
        sub_data[i]["Activity_type"]="Light_PA"
    if 0.173 <sub_data[i]["Moy_ENMONZ"][1] <= 0.382:
        sub_data[i]["Activity_type"]="Moderate_PA"
    if sub_data[i]["Moy_ENMONZ"][1] > 0.382:
        sub_data[i]["Activity_type"]="Vigourous_PA"        

# Definition de la couleur de l'epoch selon son type d'activité 

def coloriseepoch(epoch,plot_subplot):
    for i in range(len(epoch)):
        x1=epoch[i].index[0]
        x2=epoch[i].index[-1]

        graph=plot_subplot
        if epoch[i]["Activity_type"][1] == "Sedentary_PA":
            graph.axvspan(x1, x2, facecolor='aqua')
        elif epoch[i]["Activity_type"][1] == "Light_PA":
            graph.axvspan(x1, x2, facecolor='green')
        elif epoch[i]["Activity_type"][1] == "Moderate_PA":
            graph.axvspan(x1, x2, facecolor='orange')
        elif epoch[i]["Activity_type"][1] == "Vigourous_PA":
            graph.axvspan(x1, x2, facecolor='red')

#calcul de la vitesse par integration de enmo
# integrales_enmo_list=[] #Liste des valeurs d'integrales des epoch d'enmo

# for i in epochs_enmo: #Calcul de l'intégrale de enmo sur chacune des epoch definies dans epochs_enmo
#     #print(i)
#     integrale_epoch_i=sp.integrate.simpson(i,dx=5) #Calcul de l'integrale sur l'epoch i
#     integrales_enmo_list.append(integrale_epoch_i) #ajout de la valeur de l'integrale pour l'epoch i a la liste des integrales


#Affichage des graphes
plt.figure(1,figsize=(70, 3))


plt.subplot(411)
plt.plot(time, ax, '-b', lw=0.5, label ="x") #suivants mis en commentaires pour tester sur une donnée (ici x) sinon trop long à afficher
plt.title('Accelerations en fonction du temps de '+ fname)
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
plt.plot(time, enmo, 'black', lw=0.5, label ="enmo")
plt.xlabel("temps")
plt.legend(['ENMO'],loc = 'upper right')

#Coloration des zones d'activité sur le subplot choisi
coloriseepoch(sub_data,plt.subplot(414))
plt.show()





