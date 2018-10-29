from insights_connexion.db.gino import Column, Model, UUID

class Host(Model):
    __tablename__ = 'hosts'

    id = db.Column(UUID, primary_key=True)
