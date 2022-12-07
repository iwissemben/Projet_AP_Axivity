
# Projet Activité Physique: Tracker Axivity

 Ce Github repository est dédié au projet de l'UE HAH913E Activité Physique concernant le tracker d'activité Axivity AX3

# Utilisation 
Il vaut mieux avoir un jeu de donné échantillonné à 10 Hz. Si ce n'est pas le cas, des fichiers exmples sont à votre disposition. Sinon, la fonction "Resampler" peut aider. Il suffit de placer un jeu de donnée au format .csv dans /dat/Raw, mettre le nom du fichier à échantillonner dans la variable fname du fichier Resampler. Le jeu de donnée sortant se trouvera dans /dat/Converted sous le nom "Resampled_(nom d'origine du fichier)".

Vous pouvez ensuite ouvrir le fichier main dans /src et mettre le nom de votre fichier échantilloner à 10 Hz dans la variable fname.
Vous pouvez maintenant lancer main.

## Organisation du repertoire src

Le repertoire src est l'un des sous dossier du reporsitory 'Projet_AP_Axivity'


Ce dossier src contient les fichiers source/codes au format `.ipynb` ou `.py`


## FAQ
#### Peut on co-ecrire le script python?
Oui! C'est tout l'interet de GitHub. Il est possible de creer chacun sa branche pour editer le meme fichier et proposer des modifications via les pull request.
Cela permet de garder tout un historique des modifications, que chacun des contributeurs peut aprouver afin d'avancer plus vite.

#### Chaque contributeur peut il posseder son propre script?
Oui c'est possible, mais ca n'est pas forcement le plus efficace.


#### D'autres questions?


## Feedback

Si vous avez des suggestions, ou decouvrez des informations pouvant etre pertinentes pour tous, n'hesitez pas à éditer la FAQ du fichier 'readme.md' afin d'en faire profiter tout le monde.
Vous pourrez toujours faire des Pull Request afin d'alerter les autres contributeurs des changements et piquer leur curiosité.
