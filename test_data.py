
base_url = "https://petstore.swagger.io"

firstName = "testing"
lastName = "automation"
email = "testing@test.com"
password = "123456"
phone = "081100223344"
userStatus = 0


def create_user_payload(username):
    return {
        "id": 0,
        "username": username,
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": userStatus
    }

def create_user_headers():
    return {
        "Content-Type": "application/json",
        "accept": "application/json"
    }