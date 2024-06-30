using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using Newtonsoft.Json;
using System;
using TMPro;
using Unity.VisualScripting;

public class DownloadMaze : MonoBehaviour
{
    [SerializeField] private Maze _maze;
    //variables de configuraci n
    //establecer una variable
    [SerializeField] private GameObject wallPrefab;
    [SerializeField] private GameObject player;
    [SerializeField] private GetPlayerParams playerParams;

    [SerializeField] private GameObject HeightParameterUI;
    [SerializeField] private GameObject WidthParameterUI;
    [SerializeField] private GameObject SeedParameterUI;
    [SerializeField] private GameObject IterationsParameterUI;


    [SerializeField] private GameObject parameterPanel;
    [SerializeField] private TMP_Text messageText;

    private string baseUrl = "http://127.0.0.1:8000/dungeon";
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

        newEndpoint = PlayerPrefs.GetString("Endpoint", "prim");


        List<String> SizeableDungeons = new List<String> { "prim", "eller", "kruskal", "binary", "aldous-broder", "dfs" };
        List<String> IterativeDungeons = new List<String> { "tesselation" };
        List<String> SizeableIterativeDungeons = new List<String> { "cellular" };

        if (SizeableDungeons.Contains(newEndpoint))
        {
            IterationsParameterUI.SetActive(false);
        }
        else if (IterativeDungeons.Contains(newEndpoint))
        {
            HeightParameterUI.SetActive(false);
            WidthParameterUI.SetActive(false);
        }

    }

    public void generateMaze()
    {
        try
        {

            Debug.Log("Endpoint: " + PlayerPrefs.GetString("Endpoint", "prim"));
            String dungeonType = PlayerPrefs.GetString("Endpoint", "prim");
            IDungeonParameters dungeonParameters = playerParams.GetDungeonParameters();
            parameterPanel.SetActive(false);
            StartCoroutine(requestDungeon(dungeonType, dungeonParameters));

        }
        catch (InvalidParametersException)
        {
            messageText.color = Color.red;
            messageText.text = "Parámetros inválidos";
        }
        catch (Exception)
        {
            messageText.color = Color.red;
            messageText.text = "Error generando el laberinto";
        }

    }

    private IEnumerator requestDungeon(String dungeonType, IDungeonParameters dungeonParameters)
    {
        messageText.color = Color.black;
        messageText.text = "Generando laberinto...";
        String url = $"{baseUrl}/{dungeonType}{dungeonParameters.toQueryParameters()}";

        Debug.Log(url);
        using (UnityWebRequest webRequest = UnityWebRequest.Get(url))
        {
            yield return webRequest.SendWebRequest();

            if (webRequest.result == UnityWebRequest.Result.ConnectionError ||
                webRequest.result == UnityWebRequest.Result.ProtocolError)
            {
                //Debug.LogError("Error: " + webRequest.error);
                messageText.color = Color.red;
                messageText.text = "Parámetros de laberinto inválidos";
                parameterPanel.SetActive(true);
            }
            else
            {

                Debug.Log("Response received");

                if (webRequest.responseCode != 200)
                {
                    Debug.Log("Parámetros de petición inválidos");
                    messageText.color = Color.red;
                    messageText.text = "Parámetros de laberinto inválidos";

                }
                else
                {
                    var text = webRequest.downloadHandler.text;
                    try
                    {
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


    }


    void RandomFillMap()
    {


        var height = _maze.maze[0].Length;
        var width = _maze.maze.Length;

        bool playerPlaced = false;
        //System.Random pseudoRandom = new System.Random(seed.GetHashCode());

        for (int x = 0; x < width; x++)
        {
            for (int y = 0; y < height; y++)
            {
                if (_maze.maze[x][y] == 0)
                {

                    // GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
                    // cube.name = "cubo";
                    // BoxCollider collider = cube.AddComponent<BoxCollider>();
                    // collider.center = cube.transform.position;
                    // collider.size = new Vector3(1, 1, 1);
                    // Renderer renderer = cube.GetComponent<Renderer>();
                    // renderer.material.color = _maze.maze[x][y] == 1 ? Color.black : Color.white;
                    GameObject wall = Instantiate(wallPrefab, new Vector3(x, 0, y), Quaternion.AngleAxis(90, Vector3.right));
                    wall.GetComponent<Renderer>().material.color = Color.white;
                }
                else if (!playerPlaced && _maze.maze[x][y] == 1)
                {
                    Debug.Log($"Jugador colocado en {x}-{y}");
                    //player.transform.position = new Vector3(x, -0.5f, y);
                    player.transform.position = new Vector3((float)x, -0.5f, (float)y);
                    playerPlaced = true;
                }
            }
        }


        for (int x = -1; x <= width; x++)
        {
            GameObject cube = wallPrefab;

            Instantiate(cube, new Vector3(x, 0, height), Quaternion.identity).GetComponent<Renderer>().material.color = Color.grey;
            Instantiate(cube, new Vector3(x, 0, -1), Quaternion.identity).GetComponent<Renderer>().material.color = Color.grey;

        }

        for (int y = -1; y <= height; y++)
        {
            GameObject cube = wallPrefab;
            Instantiate(cube, new Vector3(width, 0, y), Quaternion.identity).GetComponent<Renderer>().material.color = Color.grey;
            Instantiate(cube, new Vector3(-1, 0, y), Quaternion.identity).GetComponent<Renderer>().material.color = Color.grey;

        }

        messageText.text = "";
    }
}
