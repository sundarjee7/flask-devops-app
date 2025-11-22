from app import app

def test_home_status_code():
    # Test if the login page loads successfully
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_home_content():
    # Test if the login page contains "Login" text
    response = app.test_client().get('/')
    assert b"Login" in response.data

