using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace dungeonGenerator
{
    internal class Dungeon
    {
        private int width;
        private int height;
        private int cellWidth;
        private int cellHeight;
        //private Cell cell;


        public Dungeon(int width, int height, int cellWidth, int cellHeight)
        {
            this.width = width; 
            this.height = height;  
            this.cellWidth = cellWidth;
            this.cellHeight = cellHeight;
        }

        public int Width()
        {
            return width;

        }

        public int Height()
        {
            return height;
        }

        public int CellWidth()
        {
            return cellWidth;
        }

        public int CellHeight()
        {
            return cellHeight;
        }
        
    }
}
