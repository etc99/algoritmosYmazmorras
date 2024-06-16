from dungeon_api.models.complete_dungeon import DungeonResponse
from typing import Optional

async def obtain_dungeon(dungeon_type: type, seed: Optional[int] = None, **kwargs) -> DungeonResponse:


    if seed:
        stored_dungeon = await DungeonResponse.find_one(DungeonResponse.algorithm == dungeon_type.__name__,
                                                    DungeonResponse.seed == seed,
                                                    DungeonResponse.parameters == kwargs)

        if stored_dungeon:
            print('Dungeon ya almacenada en base de datos')
            return stored_dungeon

    dungeon = dungeon_type(seed=seed, **kwargs)
    
    generated_dungeon = DungeonResponse(algorithm=dungeon_type.__name__, seed=dungeon.seed, parameters=kwargs, maze=dungeon.serialize_grid())
    print('Creada Dungeon')
    await generated_dungeon.insert()
    return generated_dungeon


