import requests


class apiMap:

    config = {
        'token': {
            'url': 'https://restful-booker.herokuapp.com/auth',
            'headers': {
                'Content-type': 'application/json'},
            'data': {
                'username' : 'admin',
                'password' : 'password123'
            }
        }

    }


    def __init__(self, username: str = "admin", password: str = "password123"):        
        apiMap.config['token']['data']['username'] = username
        apiMap.config['token']['data']['password'] = password

        self.username = username
        self.password = password
        self.session = self._get_session()
        self.token = self._get_token()


    def _get_session(self) -> str:
        session = requests.Session()
        return session.post(
            url=self.config['token']['url'],
            # headers=self.config['token']['headers'],
            data=self.config['token']['data'],
        )

    def _get_token(self) -> str:
        session = requests.Session()
        response = session.post(
            url=self.config['token']['url'],
            # headers=self.config['token']['headers'],
            data=self.config['token']['data'],
        )
        return response.json()['token']


test = apiMap()
print(test.token)
