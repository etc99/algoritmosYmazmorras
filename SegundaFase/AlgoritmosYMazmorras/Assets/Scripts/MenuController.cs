using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MenuController : MonoBehaviour
{
    public void StartGame()
    {
        SceneManager.LoadScene("SelectMenu");
    }

    public void PrimButton()
    {
        string endpoint = "\\" + "prim";
        PlayerPrefs.SetString("Endpoint", endpoint);
        PlayerPrefs.Save();
        SceneManager.LoadScene("DungeonScreen");
    }

    public void KruskalButton()
    {
        string endpoint = "\\" + "kruskal";
        PlayerPrefs.SetString("Endpoint", endpoint);
        PlayerPrefs.Save();
        SceneManager.LoadScene("DungeonScreen");
    }

    public void DfsButton()
    {
        string endpoint = "\\" + "dfs";
        PlayerPrefs.SetString("Endpoint", endpoint);
        PlayerPrefs.Save();
        SceneManager.LoadScene("DungeonScreen");
    }

    public void BackToMenu()
    {
        SceneManager.LoadScene("MainScreen");
    }

    public void ExitGame()
    {
        Application.Quit();
    }
}
