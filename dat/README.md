
# Projet Activité Physique: Tracker Axivity

 Ce Github repository est dédié au projet de l'UE HAH913E Activité Physique concernant le tracker d'activité Axivity AX3

## Organisation du repertoire dat

Le repertoire dat est l'un des sous dossier du reporsitory `Projet_AP_Axivity`.


Ce sous dossier  dat contient deux sous dossiers: 
- Raw : Pour les fichiers de données au format `.cwa` 
- Converted : Pour les fichiers de données converties au format `.csv` 

## FAQ
#### Pourquoi enregistrer le fichier au format .cwa du tracker?
Ce fichier permet de conserver a la fois les données correspondant au signal mais egalement les parametres d'enregistrement (frequence d'echantillonage, unités). Grace à ce fichier `.cwa` nous pourrons exporter nos données au format `.csv` en gardnant la possibilité de changer le format des données. 

/!\ Il s'agit aussi d'une sauvegarde nous protegant de la modification de nos données brutes.

#### Comment extraire un fichier au format cwa du tracker?
Voir la section  telechargement des données de la [https://github.com/digitalinteraction/openmovement/wiki/AX3-GUI#downloading-the-data](page GitHub) du logiciel OmGui.


#### Comment exporter les données au format .csv ?
Voir cette section de la [https://github.com/digitalinteraction/openmovement/wiki/AX3-GUI#exporting-to-a-comma-separated-value-csv-file](page GitHub) du logiciel OmGui.

#### D'autres questions?

## Feedback

Si vous avez des suggestions, ou decouvrez des informations pouvant etre pertinentes pour tous, n'hesitez pas à éditer la FAQ du fichier 'readme.md' afin d'en faire profiter tout le monde.
Vous pourrez toujours faire des Pull Request afin d'alerter les autres contributeurs des changements et piquer leur curiosité.
