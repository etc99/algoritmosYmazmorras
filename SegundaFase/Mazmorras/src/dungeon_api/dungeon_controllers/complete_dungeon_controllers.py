from dungeon_api.models.complete_dungeon import CompleteDungeon
from typing import Optional

async def obtain_complete_dungeon(dungeon_type: type, seed: Optional[int] = None, **kwargs) -> CompleteDungeon:


    if seed:
        stored_dungeon = await CompleteDungeon.find_one(CompleteDungeon.algorithm == dungeon_type.__name__,
                                                    CompleteDungeon.seed == seed,
                                                    CompleteDungeon.parameters == kwargs)

        if stored_dungeon:
            return stored_dungeon

    dungeon = dungeon_type(seed=seed, **kwargs) # Generar mazmorra
    
    generated_dungeon = CompleteDungeon(algorithm=dungeon_type.__name__, seed=dungeon.seed, parameters=kwargs, maze=dungeon.serialize_grid())
    await generated_dungeon.insert()
    return generated_dungeon


