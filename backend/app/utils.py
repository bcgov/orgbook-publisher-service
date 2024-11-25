from datetime import datetime, timezone, timedelta
from multiformats import multibase
import base64
import hashlib
import validators
import re


def valid_datetime_string(datetime_string):
    try:
        datetime.fromisoformat(datetime_string)
        return True
    except:
        return False


def valid_uri(value):
    DID_REGEX = re.compile("did:([a-z0-9]+):((?:[a-zA-Z0-9._%-]*:)*[a-zA-Z0-9._%-]+)")
    if DID_REGEX.match(value) or validators.url(value):
        return True
    return False

def timestamp(minutes_forward=0):
    now = datetime.now(timezone.utc)
    delta = timedelta(minutes=minutes_forward)
    return str((now + delta).isoformat("T", "seconds"))

def generate_digest_multibase(content):
    return hashlib.sha256(content.encode()).digest()

def verkey_to_multikey(verkey):
    return multibase.encode(bytes.fromhex(f"ed01{multibase.decode(f'z{verkey}').hex()}"), "base58btc")
    
def multikey_to_jwk(multikey):
    return {
        "kty": "OKP", 
        "crv": "Ed25519",
        "x": base64.urlsafe_b64encode(multibase.decode(multikey)[2:]).decode().rstrip("=")
    }