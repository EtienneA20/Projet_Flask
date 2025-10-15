from monApp.models import Auteur
from flask_login import current_user

def test_auteurs_liste(client): #client est la fixture définie dans conftest.py
    response = client.get('/auteurs/')
    assert response.status_code == 200
    assert b'Victor Hugo' in response.data

def test_auteur_update_before_login(client):
    response = client.get('/auteurs/1/update/', follow_redirects=True) 
    assert b"Login" in response.data # vérifier redirection vers page Login

#fonction qui simule une connexion
def login(client, username, password, next_path):
    return client.post("/login/",data={"Login": username,"Password": password, "next":next_path} ,follow_redirects=True)


def test_auteur_update_after_login(client,testapp):
    with testapp.app_context():
        # user non connecté
        response=client.get('/auteurs/1/update/', follow_redirects=False) 
        
        # Redirection vers la page de login
        assert response.status_code == 302 
        
        # vérification redirection vers page Login
        assert "/login/?next=%2Fauteurs%2F1%2Fupdate%2F" in response.headers["Location"] 
        
        # simulation connexion user 
        response=login(client, "CDAL", "AIGRE", "/auteurs/1/update/")

        # Page update après connexion
        assert response.status_code == 200
        assert b"Modification de l'auteur Victor Hugo" in response.data

def test_auteur_view(client, testapp):
    with testapp.app_context():
        response = client.get("/auteurs/1/view/")
        assert response.status_code == 200
        html = response.data.decode()
        assert 'Victor Hugo' in html

from monApp.models import Auteur

def test_auteur_delete_after_login(client, testapp):
    with testapp.app_context():
        # user non connecté
        response=client.get("/auteurs/1/delete", follow_redirects=False) 
        
        # Redirection vers la page de login
        assert response.status_code == 308

        # Page delete après connexion
        response = login(client, "CDAL", "AIGRE", "/auteurs/1/delete")
        assert response.status_code == 200
        assert b"Suppression de l'auteur Victor Hugo. Etes vous sur ?" in response.data

        # suppression de l'auteur
        response = client.post("/auteur/erase/",data={"idA": 1},follow_redirects=True)  #on supprime l'auteur d'id 1 
        assert response.status_code == 200
        # Vérifier que l'auteur a été supprimé
        auteur = Auteur.query.get(1)   #on a deja créé un auteur dans conftest.py, donc on peut le supprimer sans risque
        assert auteur is None

def test_auteur_create_after_login(client, testapp):
    with testapp.app_context():
        # user non connecté
        response=client.get("/auteur/", follow_redirects=False) 
        
        # Redirection vers la page de login
        assert response.status_code == 302

        # Page auteur après connexion
        response = login(client, "CDAL", "AIGRE", "/auteur/")
        assert response.status_code == 200
        assert b"Creation d'un auteur" in response.data

        # creation d'un auteur
        response = client.post("/auteur/insert/",data={"Nom": "Emile Zola"},follow_redirects=True)
        assert response.status_code == 200

        # verifier creation
        auteur = Auteur.query.filter_by(Nom="Emile Zola").first() #prend le premier auteur avec ce nom
        assert auteur is not None