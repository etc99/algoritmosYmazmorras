using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using Newtonsoft.Json;

public class DownloadMaze : MonoBehaviour
{
    [SerializeField] private Maze _maze;
    //variables de configuración
    //establecer una variable
    private string baseUrl = "http://127.0.0.1:8000/dungeon/complete";
    private string newEndpoint = null;

    [System.Serializable]
    public class Maze
    {
        //public string name;
        //public string description;
        /*public string id;
        public string algorithm;
        public string seed;
        public int[][] dungeon_cells;
        public int[] start_position;
        public int[] exit_position;*/
        public int[][] maze;
    }
    private void Start()
    {
        if(PlayerPrefs.HasKey("Endpoint"))
        {
            string receivedEndpoint = PlayerPrefs.GetString("Endpoint");
            newEndpoint = receivedEndpoint;
        }
        else
        {
            Debug.Log("No hay endpoint en playerPrefs");
        }
    }
    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Debug.Log("Getting!");
            if(newEndpoint == null)
            {
                Debug.Log("Endpoint vacio");
            }
            else
            {
                Debug.Log(newEndpoint);
                StartCoroutine(getMaze(newEndpoint));
            }
            
        }
    }
    
    private IEnumerator getMaze(string endpoint)
    {
        string url = baseUrl + endpoint;
        url += "?height=100&width=100";
        using (UnityWebRequest webRequest = UnityWebRequest.Get(url))
        {
            yield return webRequest.SendWebRequest();

            if (webRequest.result == UnityWebRequest.Result.ConnectionError ||
                webRequest.result == UnityWebRequest.Result.ProtocolError)
            {
                Debug.LogError("Error: " + webRequest.error);
            }
            else
            {
                Debug.Log("Response received");
                var text = webRequest.downloadHandler.text;
                try{
                    Maze maze = JsonConvert.DeserializeObject<Maze>(text);
                    _maze = maze;
                    RandomFillMap();
                }
                catch (JsonException jsonEx)
                {
                    Debug.LogError("JSON Error: " + jsonEx.Message);
                }
                
            }
        } 

    }

    void RandomFillMap()
    {
        

        var height = _maze.maze[0].Length;
        var width = _maze.maze.Length;
        

        //System.Random pseudoRandom = new System.Random(seed.GetHashCode());

        for (int x = 0; x < width; x++)
        {
            for (int y = 0; y < height; y++)
            {
                if (_maze.maze[x][y] == 1)
                {

                    GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
                    BoxCollider collider = cube.AddComponent<BoxCollider>();
                    collider.center = cube.transform.position;
                    collider.size = new Vector3(1,1, 1);
                    Renderer renderer = cube.GetComponent<Renderer>();
                    renderer.material.color = _maze.maze[x][y] == 1 ? Color.black : Color.white;
                    Instantiate(cube, new Vector3(x, 0, y), Quaternion.AngleAxis(90, Vector3.right));
                }  
            }
        }
    }
}
