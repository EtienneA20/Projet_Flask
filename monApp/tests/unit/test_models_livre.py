from monApp.models import Livre
def test_livre_init():
    livre = Livre(19.99, "Le Petit Prince", "http://example.com", "http://example.com/img.jpg", 1)
    assert livre.Prix == 19.99
    assert livre.Titre == "Le Petit Prince"
    assert livre.Url == "http://example.com"
    assert livre.Img == "http://example.com/img.jpg"
    assert livre.auteur_id == 1

def test_livre_repr(testapp): #testapp est la fixture définie dans conftest.py
    with testapp.app_context():
        livre=Livre.query.get(1)
        assert repr(livre) == "<Livre (1) Le Petit Prince>"