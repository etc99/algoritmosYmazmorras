using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Dungeon 
{
    private int [,] maze ;
    public float placementThreshold;
    public int [,] Maze {get{return maze;}}
    public Dungeon(int x, int y){
        GenerateMaze(x,y);
        placementThreshold = .1f;
    }
   void GenerateMaze(int mazeSizeX, int mazeSizeY ){
        maze = new int[mazeSizeX,mazeSizeY];
        
        
        for(int i=0; i<mazeSizeX ; i++ ){
            for (int j=0; j<mazeSizeY ; j++){
                if(i ==0 || j==0|| i==mazeSizeX-1 || j==mazeSizeY-1){
                    maze[i,j] = 1; 
                }

                else if (i % 2 == 0 && j % 2 == 0)
                {
                    if (Random.value > placementThreshold)
                    {
                        
                        maze[i, j] = 1;

                        int a = Random.value < .5 ? 0 : (Random.value < .5 ? -1 : 1);
                        int b = a != 0 ? 0 : (Random.value < .5 ? -1 : 1);
                        maze[i + a, j + b] = 1;
                    }
                }
                
                
                
            }
        }
    }

    

    
   

}
