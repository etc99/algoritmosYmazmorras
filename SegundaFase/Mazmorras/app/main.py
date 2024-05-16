from fastapi import FastAPI, Depends
from app.router import router
from app.core.settings.db.sqlite import SessionLocal, engine
# from app.schemas import Base
from app.router import router
from .dungeon_prim import DungeonPrim
from .dungeon_dfs import DungeonDFS
from .dungeon_cellular import DungeonCellular
from .dungeon_random_walker import DungeonRandomWalker
import os
from app.models.users.user import User, Base

sql_uri: str = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@servidor:5432/nombre_basedatos"

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(router)


@app.get("/hello")
def read_root():
     
     return {"Hello": "World"}

@app.get("/prim")
def prim():
     prim_dungeon: DungeonPrim = DungeonPrim(100, 20)
     
     return prim_dungeon.to_dungeon_response()

@app.get("/dfs")
def dfs():
     dfs_dungeon: DungeonDFS = DungeonDFS(100,20)

     return dfs_dungeon.to_dungeon_response()

@app.get("/cellular")
def cellular():
     cellular_dungeon: DungeonCellular = DungeonCellular(30,10)

     return cellular_dungeon.to_dungeon_response()

@app.get("/walker")
def cellular():
     walker_dungeon: DungeonRandomWalker = DungeonRandomWalker(100,20)

     return walker_dungeon.to_dungeon_response()

@app.get("/")
def prim():
     prim_dungeon: DungeonPrim = DungeonPrim(100, 20)
     
     return prim_dungeon.to_dungeon_response()
