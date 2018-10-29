# from db.models import Tag
import factory
import insights_connexion.test.oatts as oatts


class TagFactory(factory.Factory):
    class Meta:
        model = Tag

    id = 'default'


async def seed():
    return ()
    # return (await TagFactory().create())


oatts.seed = seed
oatts.test()
