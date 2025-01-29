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
        try:
            token = r.json()['token']
        except:
            raise TractionControllerError('No token')
        r = requests.get(
            f'{self.endpoint}/wallet/keys/{Config.WITNESS_KEY}',
            headers={
                'Authorization': f'Bearer {token}'
            }
        )
        try:
            key = r.json()['multikey']
        except:
            raise TractionControllerError('No key')
        return token    
        
    def set_headers(self, token):
        self.headers={
            'Authorization': f'Bearer {token}'
        }
    
    def offer_credential(self, alias, cred_def_id, attributes):
        cred_offer = self.create_cred_offer(cred_def_id, attributes)
        invitation = self.create_oob_inv(
            alias=alias, 
            cred_ex_id=cred_offer['cred_ex_id'], 
            handshake=True
        )
        return invitation
    
    def create_cred_offer(self, cred_def_id, attributes):
        endpoint = f'{self.endpoint}/issue-credential-2.0/create'
        cred_offer = {
            'auto_remove': False,
            'credential_preview': {
                "@type": "issue-credential/2.0/credential-preview",
                "attributes": [
                    {
                        "name": attribute,
                        "value": attributes[attribute]
                    } for attribute in attributes
                ]
            },
            'filter': {
                'indy': {
                    'cred_def_id': cred_def_id,
                }
            }
        }
        r = requests.post(
            endpoint,
            headers=self.headers,
            json=cred_offer
        )
        try:
            return r.json()
        except:
            raise TractionControllerError('No exchange')
        
    def create_pres_req(self, name, issuer, schema_id, attributes):
        endpoint = f'{self.endpoint}/present-proof-2.0/create-request'
        pres_req = {
            'auto_remove': False,
            'auto_verify': True,
            'presentation_request': {
                'indy': {
                    'name': name,
                    'version': '1.0',
                    # 'nonce': str(randint(1, 99999999)),
                    'requested_attributes': {
                        'requestedAttributes': {
                            'names': attributes,
                            'restrictions':[
                                {
                                    'issuer_did': issuer,
                                    'schema_id': schema_id
                                }
                            ]
                        }
                    },
                    'requested_predicates': {}
                }
            }
        }
        r = requests.post(
            endpoint,
            headers=self.headers,
            json=pres_req
        )
        return r.json()
    
    def create_oob_inv(self, alias=None, cred_ex_id=None, pres_ex_id=None, handshake=False):
        endpoint = f'{self.endpoint}/out-of-band/create-invitation?auto_accept=true'
        invitation = {
            "my_label": "Orgbook Publisher Service",
            "alias": alias,
            "attachments": [],
            "handshake_protocols": [],
        }
        if pres_ex_id:
            invitation['attachments'].append({
                "id":   pres_ex_id,
                "type": "present-proof"
            })
        if cred_ex_id:
            invitation['attachments'].append({
                "id":   cred_ex_id,
                "type": "credential-offer"
            })
        if handshake:
            invitation['handshake_protocols'].append(
                "https://didcomm.org/didexchange/1.0"
            )
        r = requests.post(
            endpoint,
            headers=self.headers,
            json=invitation
        )
        try:
            return r.json()
        except:
            raise TractionControllerError('No invitation')