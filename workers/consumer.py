import asyncio
import dramatiq
from src.schemas import OrderRequest
from workers.weather_service import WeatherService

weather_service = WeatherService()


# consumer logic
@dramatiq.actor(max_retries=3)
def consume_weather_request(dummy: int):
    async def run():
        request = OrderRequest(dish_id=dummy)
        await weather_service.process_request(request)

    asyncio.run(run())