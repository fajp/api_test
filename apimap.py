import requests
import json


class ApiMap:

    config = {
        'token': {
            'url': 'https://restful-booker.herokuapp.com/auth',
            'headers': {
                'Content-type': 'application/json'},
            'data': {
                'username' : 'admin',
                'password' : 'password123'
            }
        },
        'bookings_ids': {
            'base-url': 'https://restful-booker.herokuapp.com/booking',
            'filters': {
                'first_name': 'firstname',
                'last_name': 'lastname',
                'check_in': 'checkin',
                'check_out': 'checkout'
            }
        }
    }


    def __init__(self, username: str = "admin",
                password: str = "password123"):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.token = self._get_token()


    def _get_token(self) -> str:
        response = self.session.post(
            url="https://restful-booker.herokuapp.com/auth",
            data={
                'username': self.username,
                'password': self.password,
            }
        )
        return response.json()['token']


    def get_booking_ids(self, filters: dict = {}) -> list:
        """Returns a list of bookings IDs for the given filters"""

        url = "https://restful-booker.herokuapp.com/booking"

        if bool(filters):
            url += "?"
            if 'firstname' in filters.keys():
                url += f"firstname={filters['firstname']}"
            if 'lastname' in filters.keys():
                url += f"&lastname={filters['lastname']}"

        response = self.session.get(url)
        return [id['bookingid'] for id in response.json()]

    
    def get_booking(self, id: int) -> dict:
        """Returns booking information by given id"""

        return self.session.get(
            f"https://restful-booker.herokuapp.com/booking/{id}"
        ).json()


    def create_booking(self, data: dict) -> int:
        """Returns id after creating booking"""

        response = self.session.post(
            url="https://restful-booker.herokuapp.com/booking",
            headers={'Content-Type': 'application/json'},
            data=json.dumps(data),
        )
        return response.json()['bookingid']

    
    def update_booking(self, id: int, data: dict):
        """Updates booking"""

        response = self.session.put(
            url=f"https://restful-booker.herokuapp.com/booking/{id}",
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Cookie': f'token={self.token}',
            },
            data=json.dumps(data)
        )


    def partial_update_booking(self, id: int, data: dict):
        """Partialy updates booking"""

        response = self.session.patch(
            url=f"https://restful-booker.herokuapp.com/booking/{id}",
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Cookie': f'token={self.token}',
            },
            data=json.dumps(data)
        )


    def delete_booking(self, id):
        """Delete booking by given id"""

        response = self.session.delete(
            url=f"https://restful-booker.herokuapp.com/booking/{id}",
            headers={
                'Content-Type': 'application/json',
                'Cookie': f'token={self.token}',
            },
        )
