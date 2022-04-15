using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class DungeonManager : MonoBehaviour
{
    private Dungeon dungeon ;
    public Vector2Int mazeSize;
    public Vector2Int characterPosition;
    public Text console;
    
    // Start is called before the first frame update
    void Start()
    {
        dungeon = new Dungeon(mazeSize.x, mazeSize.y);
       DrawMaze();
    }

   
    void DrawMaze(){
        string output = "";
        for(int i=0; i<mazeSize.x ; i++ ){
            for (int j=0; j<mazeSize.y ; j++){
                if(i==characterPosition.x && j== characterPosition.y){
                    output += "<color=magenta>@</color>";
                }else{
                    output += dungeon.Maze[i,j] ;
                }

            }
            output += "\n";
        }
        console.text = output;

    }
    void MovePlayer(){
         if(Input.GetKeyDown(KeyCode.W)&& characterPosition.x>0 && !CheckWall(characterPosition.x-1,characterPosition.y)){

            characterPosition.x -= 1;
            DrawMaze();
        }
        if(Input.GetKeyDown(KeyCode.S)&& characterPosition.x<mazeSize.x-1 && !CheckWall(characterPosition.x+1,characterPosition.y)){
            characterPosition.x += 1;
            DrawMaze();
        }
        if(Input.GetKeyDown(KeyCode.A)&& characterPosition.y>0 && !CheckWall(characterPosition.x,characterPosition.y-1)){
            characterPosition.y -= 1;
            DrawMaze();
        }
        if(Input.GetKeyDown(KeyCode.D)&& characterPosition.y<mazeSize.y-1 && !CheckWall(characterPosition.x,characterPosition.y+1)){
            characterPosition.y += 1;
            DrawMaze();
        }
    }
    bool CheckWall(int x, int y){
        if(dungeon.Maze[x,y]== '#'){
            return true;
        }
        return false;
    }
    // Update is called once per frame
    void Update()
    {
       
        MovePlayer();
    }
}
