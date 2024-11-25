from fastapi import Request, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, APIKeyHeader
from config import settings
import jwt
import time


X_API_KEY = APIKeyHeader(name="X-API-Key")

def check_api_key_header(x_api_key: str = Depends(X_API_KEY)):
    """Check api key"""

    if x_api_key == settings.TRACTION_API_KEY:
        return True
    raise HTTPException(
        status_code=401,
        detail="Invalid API Key",
    )


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM]
        )
        return decoded_token if decoded_token["expires"] >= int(time.time()) else None
    except:
        return {}
    
    
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid or expired token")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid or expired token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid or expired token")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid