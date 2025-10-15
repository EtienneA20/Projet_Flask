**Audor Etienne**  
**groupe 2A**

# Projet_Flask  

> **Commande  bash utile:**  
> *pip freeze > requirement.txt*  
> *flask run*  
> *source venv/bin/activate*  
> *flask loaddb monApp/data/data.yml*  
> *flask newuser Cricri azerty123*  
> *flask newpasswrd Cricri legarsdu41*  
> *coverage run -m pytest*  
> *coverage report -m*  
> *coverage html*  


## Cours du 3/09: (tp1)  

paramettre du depot git  
mise en place du venv avec les diffrentes instalations  
création de 2 page web vide  
utilisation des bonnes pratique en flask   




## Cours du 10/09: (tp2)  

mise en place de la base de données avec
les 2 classes et le jeu de données recuperer sur celene  
interaction avec la base dans le terminal afin de faire des requetes type sql en commande pyton  



## Cours du 17/09:  (tp3, tp4)  

création du premier templates (index) avec un code html  
ajout d'un fichier style.css que j'ai relié à la page html  
ajout de la page contact ( fin tp1)  
création et liaison d'un fichier html pour la page contact et about  
mise en place d'un heritage entre les 3 fichier html pour factoriser le code  (le principe de bloc)
gestion des url dynamiques  

## Cours du 24/09: (tp4)

Recuperation des images et utilisation des objets Livre et Auteur  
création d'une page d'affichage simple pour mettre un tableau d'auteur avec leur information  
meme chose pour un tableau de livre  
amélioration de l'interface grace au nouveau template base.html et l'ajout
de variable dans le fichier style.css  

## Cours du 01/10: (tp5)

Instalation de flack wtf  
Utilisation de flaskForm sur la table Auteur  
Ajout d'un module pour voir un auteur  
Ajout d'un autre module pour le modifier via la liste d'auteur  
Ajout d'un bouton supprimer  
Liaison avec un template et une fonction pour interagir avec la base de donnée  
Debut de l'ajout des memes fonctionnalité avec la table Livre  

## Cours du 08/10: (tp5, tp6)

correction de la page about et contact (css)  
fin de la page viewLivre avec le detail du livre  
fin de la page updateLivre qui redirige vers viewLivre une fois le pri validé  
ajout de la commande syncdb  
ajout de la commande newpasswrd  

## travail maison du 12/10: (tp6, tp7)

mise en place du login fonctionnel  
suppression des fonction d'edition,d'insetion et de suppression d'auteurs et de livres
si l'utilisateur n'est pas connecter  
redirection vers une page de login si un utilisateur non connecter veut acceder a une
page interdite via l'URL  
redirection vers la page associé a l'action choisi juste avant de s'etre connecté  
initialisation de pytest  
debut des tests sur Auteur  

## travail du 15/10: (tp7 + bonnus)

mise en place d'une barriere pour empecher l'ajout d'un auteur avec le meme nom  
affichage des livres ecrit par chaque auteurs  

## travail maison du 15/10: (tp7)

test sur les attribut de la Class et table Livre  
test sur les attribut de la Class et de la table User  
test des routes pour la gestion et modification des auteurs  
test sur la redirection des routes après l'identification  
test sur view Auteur  
test sur suppression d'un auteur avant et après l'identification  
test sur la creation des auteurs  
test sur tout les commandes flask (loaddb,syncdb,newuser,newpasswrd)  

## Score final pytest **88%**
### Detail :
>Name                 Stmts   Miss  Cover   Missing
>--------------------------------------------------
>monApp\app.py           11      0   100%  
>monApp\commands.py      53      0   100%  
>monApp\forms.py         25      0   100%  
>monApp\models.py        33      0   100%  
>monApp\views.py        126     29    77%   : 14-18, 22, 27, 59, 74, 79, 102-103, 107-109, 114-116, 120-130, 151-152, 155  
>--------------------------------------------------  

