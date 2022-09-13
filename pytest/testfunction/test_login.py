import pytest



@pytest.fixture(scope="session")
def setUp():
    print("opening URL to login")
    yield
    print("closing after login")

def test_loginbymail(setUp):
    print("this is login by email")

def test_loginbyfacebook(setUp):
    print("this is login by facebook")


# import pytest
#
# @pytest.fixture()
# def setUp():
#     print("opening URL to login")
#     yield
#     print("closing after login")
#
# def test_loginbymail(setUp):
#     print("this is login by email")
#
# def test_loginbyfacebook(setUp):
#     print("this is login by facebook")