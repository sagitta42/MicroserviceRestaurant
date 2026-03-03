import asyncio

from src.schemas import OrderRequest, OrderResponse

class Stove:
    async def fry(self, dish_id: int):
        # simulate async DB write
        await asyncio.sleep(0.2)

        ret = OrderResponse(dish_id=dish_id, ready=True)
        print(ret)
        return ret
    
stove = Stove()