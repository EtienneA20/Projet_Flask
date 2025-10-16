def test_index(client): #client est la fixture définie dans conftest.py
    response = client.get('/index/')
    assert response.status_code == 200

def test_index_nameparam(client): #client est la fixture définie dans conftest.py
    response = client.get('/index/?name=Cricro')
    assert response.status_code == 200

def test_about(client): #client est la fixture définie dans conftest.py
    response = client.get('/about/')
    assert response.status_code == 200

def test_contact(client): #client est la fixture définie dans conftest.py
    response = client.get('/contact/')
    assert response.status_code == 200

def test_livres(client): #client est la fixture définie dans conftest.py
    response = client.get('/livres/')
    assert response.status_code == 200

def test_livre_view(client, testapp):
    response = client.get("/livres/1/view/")
    assert response.status_code == 200
        