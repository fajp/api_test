import requests

session = requests.Session()
response = session.post(
    url="https://restful-booker.herokuapp.com/auth",
    data={
        "username" : "admin",
        "password" : "password123"
    }
)
print(response.json())


session = requests.Session()
response = session.get("https://restful-booker.herokuapp.com/booking")
print(response.json())
