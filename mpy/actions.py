# actions.py
import asyncio
import httpx
from modularity import ModularityBase
from typing import Type

class Action(ModularityBase):
    @abstractmethod
    def __call__(self):
        pass

class Poller(Action):
    TResult: Type
    latency: float = 1

    async def __call__(self, src: str):
        async with httpx.AsyncClient() as client:
            while (response := await client.get(src)).is_success:
                print(response.json())
                await asyncio.sleep(self.latency)
