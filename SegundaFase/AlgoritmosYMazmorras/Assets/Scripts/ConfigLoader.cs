using System.IO;
using UnityEngine;

public class ConfigLoader : MonoBehaviour
{
    public GameConfig config;

    void Start()
    {
        string path = "config.json";
        if (File.Exists(path))
        {
            string json = File.ReadAllText(path);
            config = JsonUtility.FromJson<GameConfig>(json);
        }
        else
        {
            Debug.LogError("Archivo de configuración no encontrado.");
        }
    }
}