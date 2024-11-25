from fastapi import HTTPException
from config import settings
from app.plugins.traction import TractionController
import requests


class OrgbookPublisher:
    def __init__(self):
        self.api = settings.ORGBOOK_API_URL
        self.orgbook = settings.ORGBOOK_URL
        self.vc_service = settings.ORGBOOK_VC_SERVICE

    def fetch_buisness_info(self, identifier):
        r = requests.get(
            f"{settings.ORGBOOK_API_URL}/search/topic?q={identifier}&inactive=false&revoked=false"
        )
        buisness_info = r.json()["results"][0]
        return {
            "id": f"{settings.ORGBOOK_URL}/entity/{identifier}/type/registration.registries.ca",
            "name": buisness_info["names"][0]["text"],
        }

    async def create_credential_type(self, credential_registration):
        # TODO, better method for getting verification method
        issuer = credential_registration["issuer"]
        verification_method = f"{issuer}#key-01-multikey"

        credential_type = {
            "format": "vc_di",
            "type": credential_registration["type"],
            "issuer": credential_registration["issuer"],
            "version": credential_registration["version"],
            "verificationMethods": [verification_method],
            "cardinality": [
                {"path": credential_registration["core_paths"]["cardinalityId"]},
            ],
            "topic": {
                "type": "registration.registries.ca",
                "sourceId": {"path": credential_registration["core_paths"]["entityId"]},
            },
            "mappings": [
                {"path": "$.validFrom", "type": "effective_date", "name": "validFrom"},
                {"path": "$.validUntil", "type": "expiry_date", "name": "validUntil"},
            ],
        }
        proof_options = {
            "type": "DataIntegrityProof",
            "cryptosuite": "eddsa-jcs-2022",
            "proofPurpose": "assertionMethod",
            "verificationMethod": verification_method,
        }
        traction = TractionController()
        traction.authorize()
        signed_vc_type = traction.add_di_proof(credential_type, proof_options)
        request_body = {"securedDocument": signed_vc_type}

        r = requests.post(f"{self.vc_service}/credential-types", json=request_body)
        try:
            return r.json()
        except:
            raise HTTPException(
                status_code=400, detail="Couldn't register credential type."
            )

    async def forward_credential(self, vc, credential_registration):
        payload = {
            "securedDocument": vc,
            "options": {
                "format": "vc_di",
                "type": credential_registration["type"],
                "version": credential_registration["version"],
                "credentialId": vc["id"],
            },
        }
        r = requests.post(f"{self.vc_service}/credentials", json=payload)
        try:
            return r.json()
        except:
            raise HTTPException(
                status_code=400, detail="Couldn't register credential type."
            )
