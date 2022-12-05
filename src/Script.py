import csv
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime
#<<<<<<< HEAD
#filepath=path=os.path.normpath("../dat/Raw/")

#Importation du fichier CSV
fname = "Fichier_test_2.csv"
filepath=os.path.join("../dat/Raw/", fname)
data=pd.read_csv(filepath, sep=",",names=["date","Ax","Ay","Az"])

#conversion temps unix en human readable
data['date'] = pd.to_datetime(data['date'],unit='s')
data=data.set_index('date')

#initialisation parametres
#Fs=len(data)/(time.iloc[-1]-time.iloc[0]) #Calcul de la fréquence d'echantillonage du signal

data=data.resample('0.01S').mean() #resampling à 100Hz (moyenne des valeurs sur 1/100s )

#Initialisation des variables temps et accélération
time=data.index
x=data.iloc[:,0]
y=data.iloc[:,1]
z=data.iloc[:,2]

enmo = np.sqrt(x*x + y*y + z*z) -1  # -1 car on soustrait la gravité (1g)


#Affichage des graphes
plt.figure(1)
plt.figure(figsize=(9, 3))

plt.subplot(411)
plt.plot(time, x, '-b', lw=0.5, label ="x") #suivants mis en commentaires pour tester sur une donnée (ici x) sinon trop long à afficher
plt.title('accelerations en fonction du temps')
plt.xlabel("temps en s")
plt.legend(['ax'],loc = 'upper right')

plt.subplot(412)
plt.plot(time, y, '-r', lw=0.5, label ="y")
plt.xlabel("temps en s")
plt.legend(['ay'],loc = 'upper right')

plt.subplot(413)
plt.plot(time, z, '-c', lw=0.5, label ="z")
plt.xlabel("temps en s")
plt.legend(['az'],loc = 'upper right')

plt.subplot(414)
plt.plot(time, enmo, '-m', lw=0.5, label ="enmo")
plt.xlabel("temps en s")
plt.legend(['ENMO'],loc = 'upper right')



