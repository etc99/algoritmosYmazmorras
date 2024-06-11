using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MenuController : MonoBehaviour
{
    public void StartGame()
    {
        string endpoint = "\\" + "prim";
        PlayerPrefs.SetString("Endpoint", endpoint);
        PlayerPrefs.Save();
        SceneManager.LoadScene("DungeonScreen");
    }

    public void PrimButton()
    {
        string endpoint = "\\" + "prim";
        PlayerPrefs.SetString("Endpoint", endpoint);
        PlayerPrefs.Save();
        SceneManager.LoadScene("DungeonScreen");
    }

    public void ExitGame()
    {
        Application.Quit();
    }
}
