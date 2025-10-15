import pytest
import os
from hashlib import sha256
from monApp import db
from monApp.models import User

def test_loaddb_command(testapp):
    runner = testapp.test_cli_runner()
    path_to_file = os.path.join(os.path.dirname(__file__), "../../data/data.yml")
    path_to_file = os.path.abspath(path_to_file)    #permet de recuperer le chemin relatif du fichier data.yml
    result = runner.invoke(args=["loaddb",path_to_file])    #cette fonction predefini permet d'executer une commeande flask
    assert "Database initialized!" in result.output
    
def test_syncdb_command(testapp):
    runner = testapp.test_cli_runner()
    result = runner.invoke(args=["syncdb"])
    assert "Database synchronized!" in result.output

def test_newuser_command(testapp):
    runner = testapp.test_cli_runner()
    login = "testuser"
    pwd = "mdptest"
    result = runner.invoke(args=["newuser", login, pwd])
    assert f"User {login} created!" in result.output

    with testapp.app_context():
        user = User.query.get(login)
        assert user is not None
        # vérifier que le mot de passe est hashé
        m = sha256(); m.update(pwd.encode()); expected_hash = m.hexdigest()
        assert user.Password == expected_hash

def test_newpasswrd_command(testapp):
    runner = testapp.test_cli_runner()
    login = "userupdate"
    old_pwd = "oldpwd"
    new_pwd = "newpwd"
    # créer l'utilisateur avant de changer le mot de passe
    with testapp.app_context():
        from hashlib import sha256
        m = sha256(); m.update(old_pwd.encode()); old_hash = m.hexdigest()
        user = User(Login=login, Password=old_hash)
        db.session.add(user)
        db.session.commit()

    # mettre à jour le mot de passe via la commande
    result = runner.invoke(args=["newpasswrd", login, new_pwd])
    assert result.exit_code == 0
    assert f"User {login} updated!" in result.output

    with testapp.app_context():
        user = User.query.get(login)
        m = sha256(); m.update(new_pwd.encode()); new_hash = m.hexdigest()
        assert user.Password == new_hash
