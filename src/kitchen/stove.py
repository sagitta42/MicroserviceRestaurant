import asyncio

class Stove:
    async def fry(self, dish_id: int):
        # simulate async DB write
        await asyncio.sleep(0.2)

        # FIXME: improve
        return True

stove = Stove()
