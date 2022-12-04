# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:09:24 2022

@author: iWiss
"""
import os
import csv
import pandas as pd

#Importation du fichier CSV
filepath=os.path.normpath("C:/Users/iWiss/Desktop/donnee/Classeur1.csv")
data=pd.read_csv(filepath, sep=",",names=["Temps_unix","Ax","Ay","Az"])

#Initialisation des variables
Times=data.iloc[:,0]
Ax=data.iloc[:,1]
Ay=data.iloc[:,2]
Az=data.iloc[:,3]
