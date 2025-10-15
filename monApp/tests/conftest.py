import pytest
from monApp import app,db
from monApp.models import Auteur, Livre, User
from hashlib import sha256

@pytest.fixture
def testapp():
    app.config.update({"TESTING":True,"SQLALCHEMY_DATABASE_URI":
    "sqlite:///:memory:","WTF_CSRF_ENABLED": False})
    with app.app_context():
        db.create_all()
        # Ajouter un auteur de test
        auteur = Auteur(Nom="Victor Hugo")
        db.session.add(auteur)

        # Ajouter un livre de test
        livre = Livre(19.99, "Le Petit Prince", "http://example.com", "http://example.com/img.jpg", 1)
        db.session.add(livre)

        # Ajouter un utilisateur de test
        unUser = User(Login="usertest" ,Password ="mdptest")
        db.session.add(unUser)

        # Ajouter un autre utilisateur pour tester la simulation de connexion
        m = sha256(); m.update("AIGRE".encode()); pwd_hash = m.hexdigest()
        dalaigre = User(Login="CDAL", Password=pwd_hash)
        db.session.add(dalaigre)

        # Commit les changements
        db.session.commit()
    yield app
    # Cleanup après les tests
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(testapp):
    return testapp.test_client()
