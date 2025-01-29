from flask import current_app
from config import Config
import requests
import secrets
from random import randint


class PublisherControllerError(Exception):
    """Generic PublisherController Error."""


class PublisherController:
    def __init__(self):
        self.endpoint = Config.PUBLISHER_API_URL
        self.api_key = Config.PUBLISHER_API_KEY
        self.headers = None
        
    def admin_login(self):
        self.headers = {
            {'X-API-KEY': self.api_key}
        }
        
    def get_issuers(self):
        self.admin_login()
        r = requests.get(
            f'{self.endpoint}/registrations/issuers',
            headers=self.headers
        )
        return r.json()