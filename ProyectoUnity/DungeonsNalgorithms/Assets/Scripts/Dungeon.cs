using System.Collections;
using System.Collections.Generic;


public class Dungeon 
{
    private char [,] maze ;
    public char [,] Maze {get{return maze;}}
    public Dungeon(int x, int y){
        GenerateMaze(x,y);
    }
   void GenerateMaze(int mazeSizeX, int mazeSizeY ){
        maze = new char[mazeSizeX,mazeSizeY];
        for(int i=0; i<mazeSizeX ; i++ ){
            for (int j=0; j<mazeSizeY ; j++){
                if(i ==0 ){
                    maze[i,j] = '#';
                }else{
                   maze[i,j] = '.'; 
                }
                
                
                
            }
        }
    }
   

}
