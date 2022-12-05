import csv
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

#Paramétrage des graphes
import matplotlib as mpl
mpl.rcParams['lines.linewidth'] = 0.5
mpl.rcParams['lines.linestyle'] = '--'

#<<<<<<< HEAD
# filepath=os.path.normpath("C:/Users\Meriem\Documents\M2 IDS\activite_physique\mottet_mesure\Projet_AP_Axivity\dat")

# #Importation du fichier CSV
# fname = "47185_0000000002.csv"
# filepath=os.path.join("../dat", fname)
# data=pd.read_csv(filepath, sep=",",names=["Temps_unix","Ax","Ay","Az"])

data = pd.read_csv("C:/Users/Meriem/Downloads/data1.csv")

#Initialisation des variables temps et accélération
time=data.iloc[:,0]
x=data.iloc[:,1]
y=data.iloc[:,2]
z=data.iloc[:,3]

enmo = np.sqrt(x*x + y*y + z*z) -1  # -1 car on soustrait la gravité (1g)

plt.figure(figsize=(9, 3))

plt.plot(time, x, '-r', lw=0.4, label ="x") #suivants mis en commentaires pour tester sur une donnée (ici x) sinon trop long à afficher
plt.plot(time, y, '-b', lw=0.4, label ="y")
plt.plot(time, z, '-c', lw=0.4, label ="z")
#>>>>>>> main
