from config import settings
import requests


class OrgbookPublisher:
    """Read-only OrgBook integration: entity lookup via search API (no credential push)."""

    def fetch_buisness_info(self, identifier):
        r = requests.get(
            f"{settings.ORGBOOK_API_URL}/search/topic?q={identifier}&inactive=false&revoked=false"
        )
        buisness_info = r.json()["results"][0]
        return {
            "id": f"{settings.ORGBOOK_URL}/entity/{identifier}/type/registration.registries.ca",
            "name": buisness_info["names"][0]["text"],
        }
