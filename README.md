
# Projet Activité Physique: Tracker Axivity

 Ce Github repository est dédié au projet de l'UE HAH913E Activité Physique concernant le tracker d'activité Axivity AX3

# Utilisation
Suivez les instructions du readme dans src.


## Contributeurs

Contributions are always welcome!

Ce projet est réalisé par Ben Romdhane Wissem, Sebbata Meriem et  Molina Matthieu 
Please adhere to this project's `code of conduct`.



## Organisation du repository

Le projet AP_Axivity est organisé sous la forme d'un répertoire ayant la structure suivante: 


- 3 Sous dossiers
    - src
    - dat 
    - res
- 1 `readme.md` par dossier 
- Fichiers spécifiques à chaque dossier

Chacun des 3 sous dossiers contient son propre fichier readme permettant d'expliquer le contenu du dossier dans lequel il se situe

Le dossier src contient les fichiers source/codes au format `.ipynb` ou `.py`
Le dossier dat contient deux sous dossiers 
- Raw : contiendra les fichiers de données au format `.cwa`
- Converted : contiendra les fichiers de données converties au format `.csv`
## FAQ

#### Qu'est ce que ce tracker AX3? Qu'enregistre-t-il ?

AX3 est un enregistreur automatique composé d'un accelerometre à 3 axes. Il permet donc de relever au cours du temps des valeurs d'accelerations lorsqu'il est porté.

#### Quel est le modele du tracker d'activité sur lequel nous travaillions?

Nous travaillions sur le tracker AX3 d'Axivity. Voir la 
[Page Web tracker AX3](https://axivity.com/product/ax3) pour plus de détails sur le capteur.


#### Ou peut on trouver le manuel utilisateur du tracker?

Il existe un manuel utilisateur trouvable à cette adresse: [Manuel](https://axivity.com/userguides/ax3/)

#### Peut on programmer le capteur AX3?

Oui! c'est tout le principe, Axivity à developpé un logiciel permettant de communiquer avec le tracker et de le configurer.
Ce logiciel s'intitule OmGui, une page [GitHub](https://github.com/digitalinteraction/openmovement/wiki/AX3-GUI) à été spécialement rédigée pour comprendre comment prendre en main le logiciel et configurer le tracker AX3.

#### Comment peut on récuperer les données enregistrées par le tracker?

Voir le guide [GitHub](https://github.com/digitalinteraction/openmovement/wiki/AX3-GUI)
## Feedback

Si vous avez des suggestions, ou decouvrez des informations pouvant etre pertinentes pour tous, n'hesitez pas à éditer la FAQ du fichier 'readme.md' afin d'en faire profiter tout le monde.
Vous pourrez toujours faire des Pull Request afin d'alerter les autres contributeurs des changements et piquer leur curiosité.
