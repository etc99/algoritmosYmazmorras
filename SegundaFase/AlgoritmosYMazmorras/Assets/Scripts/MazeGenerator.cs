using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MazeGenerator : MonoBehaviour
{
    public int width;
    public int height;
    public string seed;
    public bool useRandomSeed;

    [Range(0, 100)]
    public int randomFillPercent;

    int[,] map;

    void Start()
    {
        GenerateMap();
        RandomFillMap();
    }

    void GenerateMap()
    {
        map = new int[width, height];
    }

    void RandomFillMap()
    {
        if (useRandomSeed)
        {
            seed = Time.time.ToString();
        }

        System.Random pseudoRandom = new System.Random(seed.GetHashCode());

        for (int x = 0; x < width; x++)
        {
            for (int y = 0; y < height; y++)
            {
                map[x, y] = (pseudoRandom.Next(0, 100) < randomFillPercent) ? 1 : 0;
                if (map[x, y] == 1)
                {
                    GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
                    Renderer renderer = cube.GetComponent<Renderer>();
                    renderer.material.color = map[x, y] == 1 ? Color.black : Color.white;
                    Instantiate(cube, new Vector3(x, 0, y), Quaternion.AngleAxis(90, Vector3.right));
                }
            }
        }
    }

    //private void OnDrawGizmos()
    //{
    //    if (map != null)
    //    {
    //        for (int x = 0; x < width; x++)
    //        {
    //            for (int y = 0; y < height; y++)
    //            {
    //                Gizmos.color = (map[x, y] == 1) ? Color.black : Color.white;
    //                Vector3 position = new Vector3(-width / 2 + x + .5f, 0, -height / 2 + y + .5f);
    //                Gizmos.DrawCube(position, Vector3.one);
    //            }
    //        }
    //    }
    //}

}
