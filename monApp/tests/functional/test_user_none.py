import pytest
from monApp.models import User
from monApp.forms import LoginForm

def test_get_authenticated_user_not_found(testapp):
    with testapp.app_context():
        form = LoginForm()
        #on simule la saisie manuel 
        form.Login.data = "n'existe pas"
        form.Password.data = "n'existe pas"
        result = form.get_authenticated_user()
        assert result is None