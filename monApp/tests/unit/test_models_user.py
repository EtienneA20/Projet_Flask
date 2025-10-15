from monApp.models import User, load_user
def test_User_init():
    testuser = User(Login="loginuser", Password="securepassword")
    assert testuser.Login == "loginuser"
    assert testuser.Password == "securepassword"

def test_User_login(testapp):
    with testapp.app_context():
        user=User.query.get("usertest")
        assert user.get_id() == "usertest"
        assert user.Password == "mdptest"
        loaded_user = load_user("usertest")
        assert loaded_user is not None
        assert loaded_user.Login == "usertest"