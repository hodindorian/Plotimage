<div align = center>

<img src="https://cdn.discordapp.com/attachments/691567945825910795/1205062510634467348/python_plush.png?ex=65d700eb&is=65c48beb&hm=9b10e8f79877e74c0f9077b0873bf5cde7670c1781f514553d51ae59abc5e83c&" width="1080" height="">

# **Plotimage**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
</div>


# Présentation

Ce projet a pour but de gérer des images sur un site Internet. On a la possibilité de transformer une image en noir et blanc, en nuance de gris, la redimensionner, aligner deux images verticalement et horizontalement, fusion deux images et faire un diaporama avec différentes images.

# Développeurs

- Corentin RICHARD : corentin.richard@etu.uca.fr
- Dorian HODIN : dorian.hodin@etu.uca.fr

<div align="center">
<a href = "https://codefirst.iut.uca.fr/git/corentin.richard">
<img src="https://codefirst.iut.uca.fr/git/avatars/4372364870f18ab9104f13222fa84d2e?size=870" width="50" >
</a>
<a href = "https://codefirst.iut.uca.fr/git/dorian.hodin">
<img src="https://codefirst.iut.uca.fr/git/avatars/d6f97dbdf66352b0b66685e144aa1ee5?size=870" width="50" >
</a>
</div>


# Lancement du projet :

* #### Pour lancer le projet, il faut faire cette commande depuis la racine du répot :

    ```cd views```

    ```python3 manage.py runserver```

* Il faut ensuite aller sur l'adresse suivante :

    ```http://127.0.0.1:8000/```

* Et vous pouvez ensuite choisir les différente actions à effectuer sur vos images !

* Cliquer sur l'une des différentes actions disponibles sur l'écran, et vous devrez ensuite séléctionner une image ou plusieurs pour les fonctions :
    * Noir et Blanc
    * Nuance de gris
    * Alignement Vertical
    * Alignement Horizontal
    * Fusion d'image

* Et pour les deux fonctions suivantes, vous devez rentrer des données avant de selectionner vos images (comme la taille ou alors le nombre d'image à prendre pour faire un diaporama) :
    * Redimensionnement
    * Diaporama


# Explication du projet :

* Le projet est divisé en deux dossiers principaux, tout d'abord le dossier src, qui contient methods.py. Ce fichier contient toutes les différentes fonctions necessaires à la modification de vos images.

* Nous avons ensuite le dossier views, qui contient toute la partie Django du projet.
    * À la racine de ce dossier, nous avons tous les différents fichiers qui permettent la configuration et le lancement de Django, et des fichiers de configurations des différentes routes (urls.py).
    * Nous avons aussi le fichier views.py, qui s'occupe d'appeler toutes les fonctions de methods.py et de traiter le resultat, pour ensuite envoyer ça aux fichiers HTML
    * Les fichiers HTML sont situés dans le dossier templates, et sont appelés par views.py. Il permettent différentes affichages en fonction du choix fait sur la page d'acceuil.
    * Dans ce dossier templates, nous avons un dossier static qui contient les différentes images utiles au projet, comme les images de fond ou bien les images générés, qui seront générés dans le dossier static/pictures/generated

* Front inspiré de ce template : https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_coming_soon&stacked=h
