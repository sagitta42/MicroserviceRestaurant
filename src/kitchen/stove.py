import asyncio

COOKING_TIMES = {1: 5, 2: 3, 3: 7, 4: 1}


class Stove:
    async def fry(self, dish_id: int):
        cooking_time = COOKING_TIMES[dish_id]
        print(f"[stove] *sizzling*")
        await asyncio.sleep(cooking_time)


stove = Stove()
