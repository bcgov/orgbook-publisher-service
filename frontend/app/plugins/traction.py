from flask import current_app
from config import Config
import requests


class TractionControllerError(Exception):
    """Generic TractionController Error."""


class TractionController:
    def __init__(self):
        self.endpoint = Config.TRACTION_API_URL
        self.tenant_id = Config.TRACTION_TENANT_ID
        self.api_key = Config.TRACTION_API_KEY
        self.headers = {}
        
    def admin_login(self, tenant_id, api_key):
        r = requests.post(
            f'{self.endpoint}/multitenancy/tenant/{tenant_id}/token',
            json={
                'api_key': api_key
            }
        )
        token = r.json()['token']
        r = requests.get(
            f'{self.endpoint}/wallet/keys/{Config.WITNESS_KEY}',
            headers={
                'Authorization': f'Bearer {token}'
            }
        )
        if not r.json()['multikey']:
            raise TractionControllerError('Wrong tenant, no witness key.')
        return token
        