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
    public void CellularButton()
    {
        string endpoint = "\\" + "cellular";
        PlayerPrefs.SetString("Endpoint", endpoint);
        PlayerPrefs.Save();
        SceneManager.LoadScene("DungeonScreen");
    }
    public void BinaryButton()
    {
        string endpoint = "\\" + "binary";
        PlayerPrefs.SetString("Endpoint", endpoint);
        PlayerPrefs.Save();
        SceneManager.LoadScene("DungeonScreen");
    }
    public void EllerButton()
    {
        string endpoint = "\\" + "eller";
        PlayerPrefs.SetString("Endpoint", endpoint);
        PlayerPrefs.Save();
        SceneManager.LoadScene("DungeonScreen");
    }
    public void AldousButton()
    {
        string endpoint = "\\" + "aldous-broder";
        PlayerPrefs.SetString("Endpoint", endpoint);
        PlayerPrefs.Save();
        SceneManager.LoadScene("DungeonScreen");
    }
    public void TesselationButton()
    {
        string endpoint = "\\" + "tesselation";
        PlayerPrefs.SetString("Endpoint", endpoint);
        PlayerPrefs.Save();
        SceneManager.LoadScene("DungeonScreen");
    }

    public void BackToMenu()
    {
        SceneManager.LoadScene("MainScreen");
    }
    public void BackToSelectionMenu()
    {
        SceneManager.LoadScene("SelectMenu");
    }
    public void ExitGame()
    {
        Application.Quit();
    }
}
