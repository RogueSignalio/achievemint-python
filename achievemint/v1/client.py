import requests
import json
from datetime import datetime, timedelta
from achievemint.errors import AuthenticationError, NotFoundError, ApiError, ClientError

class Client:
    def __init__(self, client_id, client_secret, url='https://api.achievemint.net', auth_path='/oauth/token'):
        self.api_url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_path = auth_path
        self.path_version = '/api/v1'

        self.authenticate()


    def send_request(self, path, params, response_obj):
        self.refresh_token()
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'{self.token_type} {self.token}'
        }
        response = requests.post(f'{self.api_url}{self.path_version}{path}', headers=headers, data=json.dumps(params))
        try:
            response_data = response.json()

        except ValueError:
          raise ClientError('Invalid response')

        if response_obj not in response_data:
            return response_data
        else:
            return response_data[response_obj]


    def create_user(self, name, email):
        return self.send_request('/users/create', {'name': name, 'email': email}, 'user')


    def get_user(self, id):
        return self.send_request('/users/fetch', {'id': id}, 'user')

    def get_user_achievements(self, id):
        return self.send_request('/users/achievements', {'id': id}, 'achievements')


    def get_category_template_versions(self, category_id):
        return self.send_request('/categories/template_versions', {'id': category_id}, 'template_versions')


    def award_achievement(self, template_version_id, user_id):
        return self.send_request('/achievements/award', {'template_version_id': template_version_id, 'user_id': user_id}, 'achievement')


    def authenticate(self):
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.post(f'{self.api_url}{self.auth_path}', headers={'Content-Type': 'application/json'}, data=json.dumps(body))
        try:
            response_obj = response.json()
        except ValueError:
          raise AuthenticationError('Invalid response')

        if 'error' in response_obj:
          raise AuthenticationError(response_obj['error_description'])

        self.token = response_obj['access_token']
        self.expires_at = datetime.now() + timedelta(seconds=response_obj['expires_in'])
        self.token_type = response_obj['token_type']


    def refresh_token(self):
        if not hasattr(self, 'expires_at') or datetime.now() > self.expires_at:
            self.authenticate()
  
