import asyncio


class Stove:
    async def fry(self, dish_id: int):
        # cooking time
        await asyncio.sleep(3)


stove = Stove()
