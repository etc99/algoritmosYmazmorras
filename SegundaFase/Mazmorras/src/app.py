
from enum import Enum

from fastapi import FastAPI, Request, Query
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dungeon_api.models.complete_dungeon import DungeonResponse
from typing import Literal
from dungeon_api.dungeon_generators import DungeonDFS, DungeonPrim, DungeonCellular, DungeonKruskal, DungeonBinaryTree, DungeonEller, DungeonAldousBroder, DungeonTesselation
from dungeon_api.dungeon_controllers.complete_dungeon_controllers import obtain_dungeon
from contextlib import asynccontextmanager

import sys

# Establece un nuevo límite para la recursión
nuevo_limite = 999999999
sys.setrecursionlimit(nuevo_limite)


database = AsyncIOMotorClient(
    f'mongodb://{os.getenv("MONGO_USER")}:{os.getenv("MONGO_PASS")}@{os.getenv("MONGO_HOST")}:{os.getenv("MONGO_PORT")}')

print(f'mongodb://{os.getenv("MONGO_USER")}:{os.getenv("MONGO_PASS")}@{os.getenv("MONGO_HOST")}:{os.getenv("MONGO_PORT")}')


@asynccontextmanager
async def init_db(app):
    await init_beanie(database=database.db_name, document_models=[DungeonResponse])
    yield


app = FastAPI(lifespan=init_db, title="DungeonAPI", summary="dungeons")


AvailableAlgorithms = Literal["prim", "dfs", "cellular"]


@app.get("/dungeon/prim")
async def get_prim_dungeon(request: Request, height: int = Query(), width: int = Query(), seed: int | None = Query(None)):
    return (await obtain_dungeon(DungeonPrim, seed, height=height, width=width)).model_dump()


@app.get("/dungeon/dfs")
async def get_dfs_dungeon(request: Request, height: int = Query(), width: int = Query(), seed: int | None = Query(None)):
    return (await obtain_dungeon(DungeonDFS, seed, height=height, width=width)).model_dump()


@app.get("/dungeon/cellular")
async def get_cellular_dungeon(request: Request,
                               height: int = Query(),
                               width: int = Query(),
                               seed: int | None = Query(None),
                               iterations: int | None = Query(None, gt=10, le=10_000)):
    return (await obtain_dungeon(DungeonCellular,
                                          seed,
                                          height=height,
                                          width=width,
                                          max_iterations=iterations)).model_dump()

@app.get("/dungeon/kruskal")
async def get_kruskal_dungeon(request: Request, height: int = Query(), width: int = Query(), seed: int | None = Query(None)):
    return (await obtain_dungeon(DungeonKruskal, seed, height=height, width=width)).model_dump()

@app.get("/dungeon/binary")
async def get_binary_tree_dungeon(request: Request, height: int = Query(), width: int = Query(), seed: int | None = Query(None)):
    return (await obtain_dungeon(DungeonBinaryTree, seed, height=height, width=width)).model_dump()

@app.get("/dungeon/eller")
async def get_eller_dungeon(request: Request, height: int = Query(), width: int = Query(), seed: int | None = Query(None)):
    return (await obtain_dungeon(DungeonEller, seed, height=height, width=width)).model_dump()

@app.get("/dungeon/aldous-broder")
async def get_aldous_broder_dungeon(request: Request, height: int = Query(), width: int = Query(), seed: int | None = Query(None)):
    return (await obtain_dungeon(DungeonAldousBroder, seed, height=height, width=width)).model_dump()

@app.get("/dungeon/tesselation")
async def get_tesselation_dungeon(request: Request, iterations: int = Query(4, lt=10, gt=1), seed: int | None = Query(None)):
    return (await obtain_dungeon(DungeonTesselation, seed, iters=iterations)).model_dump()
