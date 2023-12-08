using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using Newtonsoft.Json;

public class DownloadMaze : MonoBehaviour
{
    [SerializeField] private Maze _maze;
    
    [System.Serializable]
    public class Maze
    {
        public string name;
        public string description;
        public int[][] result;
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Debug.Log("Getting!");
            StartCoroutine(getMaze());
        }
    }

    private IEnumerator getMaze()
    {
        using (UnityWebRequest webRequest = UnityWebRequest.Get("http://127.0.0.1:8000/dfs"))
        {
            yield return webRequest.SendWebRequest();
            if(webRequest.isHttpError || webRequest.isNetworkError) {
                Debug.Log("ERROR: No se conecto!");
            }
            else
            {
                Debug.Log("Ok");
                var text = webRequest.downloadHandler.text;
                Maze maze =  JsonConvert.DeserializeObject<Maze>(text);
                //Debug.Log(maze.name);
                //Debug.Log(maze.description);
                Debug.Log(maze.result);
                _maze = maze;
                RandomFillMap();
            }
        } // INSTANCIACION DE USAR Y TIRAR

    }

    void RandomFillMap()
    {
        

        var height = _maze.result[0].Length;
        var width = _maze.result.Length;
        

        //System.Random pseudoRandom = new System.Random(seed.GetHashCode());

        for (int x = 0; x < width; x++)
        {
            for (int y = 0; y < height; y++)
            {
                if (_maze.result[x][y] == 1)
                {

                    GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
                    BoxCollider collider = cube.AddComponent<BoxCollider>();
                    collider.center = cube.transform.position;
                    collider.size = new Vector3(1,1, 1);
                    Renderer renderer = cube.GetComponent<Renderer>();
                    renderer.material.color = _maze.result[x][y] == 1 ? Color.black : Color.white;
                    Instantiate(cube, new Vector3(x, 0, y), Quaternion.AngleAxis(90, Vector3.right));
                }  
            }
        }
    }
}
