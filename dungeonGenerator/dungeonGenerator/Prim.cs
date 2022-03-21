using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace dungeonGenerator
{
    class Prim : DungeonInterface
    {
        

        public void generator(Dungeon dungeon)
        {
            ArrayList visited = new ArrayList();
            List<Vector> toVisit = new List<Vector>();

            visited.Add(0);
            toVisit.Add(new Vector(0, 1));
            toVisit.Add(new Vector(0, dungeon.Width()));

            while(toVisit.Count() > 0)
            {
                int rand;
            }

        }

        public void Main()
        {
            Dungeon dungeon = new Dungeon(20, 20, 5, 5);
            generator(dungeon);
        }
    }
}