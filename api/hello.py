# from db.models import Host
from insights_connexion import responses


async def search():
    return responses.get({"message": "Hello hosts inventory!"})
