using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace dungeonGenerator
{
    internal class Vector
    {
        public int start;
        public int end; 

        public Vector(int start, int end)
        {
            this.start = start; 
            this.end = end;
        }

        public String toString()
        {
            return "(" + start + "," + end +")";
        }

        public Boolean equals(Object obj)
        {
            if(!(obj.GetType() == typeof(Vector)))
            {
                return false;
            }

            Vector vec = (Vector)obj;
            return vec.start == start && vec.end == end;
        }

        public int hashCode()
        {
            return this.ToString().GetHashCode();
        }
    }
}
