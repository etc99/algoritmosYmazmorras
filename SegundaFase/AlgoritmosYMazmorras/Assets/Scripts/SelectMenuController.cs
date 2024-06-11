using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SelectMenuController : MonoBehaviour
{
    public void StartGame()
    {
        SceneManager.LoadScene("DungeonScreen");
    }

    public void AlgoritmoDePrim()
    {
        SceneManager.LoadScene("DungeonScreen");
    }
    public void BackScreen()
    {
        SceneManager.LoadScene("MainScreen");
    }
}
