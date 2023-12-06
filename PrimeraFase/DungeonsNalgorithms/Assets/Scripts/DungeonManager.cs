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
    public GameObject wallPrefab;
    public GameObject floorPrefab;
    public GameObject player;

    
    // Start is called before the first frame update
    void Start()
    {
        dungeon = new Dungeon(mazeSize.x, mazeSize.y);
        Vector2Int startPlayerPosition = new Vector2Int(0,0);
        bool flag = false;
        for(int i=0; i<dungeon.MazeSizeX; ++i){
            for(int j=0; j<dungeon.MazeSizeY; ++j){
                GameObject prefab;
                if(dungeon.Maze[i,j]==0){
                    prefab = floorPrefab;
                    if(flag==false){
                        startPlayerPosition.x = i;
                        startPlayerPosition.y = j;
                        flag = true;
                    }
                }else{
                    prefab = wallPrefab;
                }
                Instantiate(prefab,new Vector3(i,0,j),Quaternion.AngleAxis(90,Vector3.right));                
            }
        }
        Instantiate(player,new Vector3(startPlayerPosition.x,0,startPlayerPosition.y),Quaternion.AngleAxis(0,Vector3.right));
       //DrawMaze();
    }


    void DrawMaze(){
        string output = "";
        for(int i=0; i<mazeSize.x ; i++ ){
            for (int j=0; j<mazeSize.y ; j++){
                if(i==characterPosition.x && j== characterPosition.y){
                    output += "<color=magenta>@</color>";
                }else if(dungeon.Maze[i,j]==0){
                    output += '.';
                }else if(dungeon.Maze[i,j]==1){
                    output += "<color=lime>#</color>";
                }
                /*
                    output += dungeon.Maze[i,j] ;
                }*/

            }
            output += "\n";
        }
        console.text = output;

    }
    void MovePlayer(){
         if(Input.GetKeyDown(KeyCode.W)&& characterPosition.x>0 && !CheckWall(characterPosition.x-1,characterPosition.y)){
            characterPosition.x -= 1;
    
            //DrawMaze();
        }
        if(Input.GetKeyDown(KeyCode.S)&& characterPosition.x<mazeSize.x-1 && !CheckWall(characterPosition.x+1,characterPosition.y)){
            characterPosition.x += 1;
            //DrawMaze();
        }
        if(Input.GetKeyDown(KeyCode.A)&& characterPosition.y>0 && !CheckWall(characterPosition.x,characterPosition.y-1)){
            characterPosition.y -= 1;
            //DrawMaze();
        }
        if(Input.GetKeyDown(KeyCode.D)&& characterPosition.y<mazeSize.y-1 && !CheckWall(characterPosition.x,characterPosition.y+1)){
            characterPosition.y += 1;
            //DrawMaze();
        }
        player.transform.position = new Vector3(characterPosition.x,characterPosition.y,0);
    }
    bool CheckWall(int x, int y){
        if(dungeon.Maze[x,y]== 1){
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
