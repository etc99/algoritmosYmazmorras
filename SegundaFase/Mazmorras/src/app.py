
from enum import Enum

from fastapi import FastAPI, Request, Query
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dungeon_api.models.complete_dungeon import CompleteDungeon
from dungeon_api.models.iterative_dungeon import IterativeDungeon
from typing import Union, Literal
from dungeon_api.dungeon_generators import DungeonDFS, DungeonPrim
from dungeon_api.dungeon_controllers.complete_dungeon_controllers import obtain_complete_dungeon
from dungeon_api.dungeon_controllers.iterative_dungeon_controllers import obtain_iterative_dungeon
from contextlib import asynccontextmanager

print(f'mongodb://{os.getenv("MONGO_USER")}:{os.getenv("MONGO_PASS")}@{os.getenv("MONGO_HOST")}:{os.getenv("MONGO_PORT")}')
database = AsyncIOMotorClient(
    f'mongodb://{os.getenv("MONGO_USER")}:{os.getenv("MONGO_PASS")}@{os.getenv("MONGO_HOST")}:{os.getenv("MONGO_PORT")}')



@asynccontextmanager
async def init_db(app):
    await init_beanie(database=database.db_name, document_models=[CompleteDungeon, IterativeDungeon])
    yield


app = FastAPI(lifespan=init_db)


AvailableAlgorithms = Literal["prim", "dfs", "kruskal"]


@app.get("/dungeon/complete/{algorithm}")
async def get_complete_dungeon(request: Request, algorithm: AvailableAlgorithms, height: int = Query(), width: int = Query(), seed: int | None = Query(default=None)):
    algorithms_mapping = {
        "prim": DungeonPrim,
        "dfs": DungeonDFS
    }

    extra_params = {k: v for k,v in request.query_params.items() if k not in {"height", "width", "seed"}}

    return (await obtain_complete_dungeon(dungeon_type=algorithms_mapping[algorithm], **request.query_params)).serialize()

import sys

# Establece un nuevo límite para la recursión
nuevo_limite = 999999999
sys.setrecursionlimit(nuevo_limite)


# @app.get("/dungeon/iterative/{algorithm}")
# async def get_iterative_dungeon(request: Request, algorithm: AvailableAlgorithms,  height: int, width: int, seed: int | None = None):
#     algorithms_mapping = {
#         "prim": DungeonPrim,
#         "dfs": DungeonDFS
#     }
#     extra_params = {k: v for k,v in request.query_params.items() if k not in {"height", "width", "seed"}}


#     return (await obtain_iterative_dungeon(dungeon_type=algorithms_mapping[algorithm], **request.query_params)).model_dump()
