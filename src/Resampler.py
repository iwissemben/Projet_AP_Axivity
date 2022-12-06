# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:31:44 2022

@author: iWiss
"""
import os
import pandas as pd
#Script Resample 

#Importation du fichier CSV
fname = "Fichier_test_2.csv"
filepath=os.path.join("../dat/Raw/", fname)
data=pd.read_csv(filepath, sep=",",names=["date","Ax","Ay","Az"])

#conversion temps unix en human readable
data['date'] = pd.to_datetime(data['date'],unit='s')
data=data.set_index('date')

#initialisation parametres
#Fs=len(data)/(time.iloc[-1]-time.iloc[0]) #Calcul de la fréquence d'echantillonage du signal
Tr=1/10 #Periode de resampling (1/Fr)
toto="../dat/Converted/"+"Resampled_"+str(Tr)+"Hz_"+fname
data=data.resample(str(Tr)+'S').mean() #resampling à 10Hz? (moyenne des valeurs sur 1/100s )
data.to_csv("../dat/Converted/"+"Resampled_"+str(int(1/Tr))+"Hz_"+fname)