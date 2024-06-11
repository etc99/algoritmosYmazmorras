from dungeon_api.models.iterative_dungeon import IterativeDungeon
from typing import Optional


async def obtain_iterative_dungeon(dungeon_type: type, seed: Optional[int] = None, **kwargs) -> IterativeDungeon:

    stored_dungeon = await IterativeDungeon.find_one(IterativeDungeon.algorithm == dungeon_type.__name__,
                                            IterativeDungeon.seed == seed,
                                            IterativeDungeon.parameters == kwargs)
    
    if stored_dungeon:
        return stored_dungeon
    
    dungeon = dungeon_type(seed=seed, **kwargs)
    generated_dungeon = IterativeDungeon(algorithm=dungeon_type.__name__, seed=dungeon.seed, parameters=kwargs, steps=dungeon.steps)
    await generated_dungeon.insert()
    return generated_dungeon