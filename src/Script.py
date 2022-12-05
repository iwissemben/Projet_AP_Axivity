import csv
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

#<<<<<<< HEAD
#filepath=path=os.path.normpath("../dat/Raw/")

#Importation du fichier CSV
fname = "Fichier_test.csv"
filepath=os.path.join("../dat/Raw/", fname)
data=pd.read_csv(filepath, sep=",",names=["Temps_unix","Ax","Ay","Az"])

#Initialisation des variables temps et accélération
time=data.iloc[:,0]
x=data.iloc[:,1]
y=data.iloc[:,2]
z=data.iloc[:,3]

enmo = np.sqrt(x*x + y*y + z*z) -1  # -1 car on soustrait la gravité (1g)

plt.plot(time, x, '*-r', lw=1, label ="x") #suivants mis en commentaires pour tester sur une donnée (ici x) sinon trop long à afficher
#plt.plot(time, y, '*-b', lw=1, label ="y")
#plt.plot(time, z, '-*c', lw=1, label ="z")
#>>>>>>> main
