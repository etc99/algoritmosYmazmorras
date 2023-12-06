using System;
using System.Collections;
using System.Collections.Generic;
using System.Xml.Schema;
using UnityEditor;


public class Dungeon
{
    private int [,] maze ;
    public float placementThreshold;
    public int [,] Maze {get{return maze;}}
    private int mazeSizeX;
    private int mazeSizeY;
    public int MazeSizeX {get{return mazeSizeX;}}
    public int MazeSizeY {get{return mazeSizeY;}}

    public Dungeon(int x, int y){
        mazeSizeX = x;
        mazeSizeY = y;
        placementThreshold = .1f;
        GenerateMaze(mazeSizeX,mazeSizeY);
    }

    public void GenerateMaze (sizeX, sizeY){

        maze = new int[sizeX, sizeY];
        int maxX = maze.GetUpperBound(0);
        int maxY = maze.GetUpperBound(1);

        for (int i = 0; i < sizeX; i++)
        {
            for (int j = 0; j < sizeY; j++)
            {

                if (i == 0 || j == 0 || i == maxX || j == maxY)
                {
                    maze[i, j] = 1;
                }

                else if (i % 2 == 0 && j % 2 == 0)
                {
                    if (Random.value > placementThreshold)
                    {

                        maze[i, j] = 1;
                        int a, b;
                        if (Random.value < .5)
                        {
                            a = 0;
                        }
                        else
                        {
                            if (Random.value < .5)
                            {
                                a = -1;
                            }
                            else
                            {
                                a = 1;
                            }
                        }
                        if (a != 0)
                        {
                            b = 0;
                        }
                        else if (Random.value < .5)
                        {
                            b = -1;
                        }
                        else
                        {
                            b = 1;
                        }

                        maze[i + a, j + b] = 1;
                    }
                }

            }
            }
        }
    }



}
