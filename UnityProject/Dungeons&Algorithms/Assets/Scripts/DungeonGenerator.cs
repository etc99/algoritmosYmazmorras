using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class DungeonGenerator : MonoBehaviour
{
    private char [,] maze ;
    public Vector2Int mazeSize;
    public Vector2Int characterPosition;
    public Text console;
    // Start is called before the first frame update
    void Start()
    {
        GenerateMaze();

        DrawMaze();
    }

    void GenerateMaze(){
        maze = new char[mazeSize.x,mazeSize.y];
        for(int i=0; i<mazeSize.x ; i++ ){
            for (int j=0; j<mazeSize.y ; j++){
                
                maze[i,j] = '.';
                
                
            }
        }
    }

    void DrawMaze(){
        string output = "";
        for(int i=0; i<mazeSize.x ; i++ ){
            for (int j=0; j<mazeSize.y ; j++){
                if(i==characterPosition.x && j== characterPosition.y){
                    output += "<color=magenta>@</color>";
                }else{
                    output += maze[i,j] ;
                }

            }
            output += "\n";
        }
        console.text = output;

    }
    // Update is called once per frame
    void Update()
    {
        if(Input.GetKeyDown(KeyCode.W)&& characterPosition.x>0){
            characterPosition.x -= 1;
            DrawMaze();
        }
        if(Input.GetKeyDown(KeyCode.S)&& characterPosition.x<mazeSize.x-1){
            characterPosition.x += 1;
            DrawMaze();
        }
        if(Input.GetKeyDown(KeyCode.A)&& characterPosition.y>0){
            characterPosition.y -= 1;
            DrawMaze();
        }
        if(Input.GetKeyDown(KeyCode.D)&& characterPosition.y<mazeSize.y-1){
            characterPosition.y += 1;
            DrawMaze();
        }
        
    }
}
