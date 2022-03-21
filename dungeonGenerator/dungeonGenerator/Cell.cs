using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace dungeonGenerator
{
    internal class Cell
    {
        private List<int> walls ;
        private bool insideMaze;
        public Cell()
        {
            insideMaze = false;
        }

        public bool isInsideMaze()
        {
            return insideMaze;
        }
    }
}
